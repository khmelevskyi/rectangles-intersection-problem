import matplotlib.pyplot as plt

from src.utils import track_time
from src.tasks_generator import StripesConstructor
from src.algos import greedy_maximum_non_overlapping_rectangles,\
                      random_search, genetic_algorithm,\
                      bfs_search


def comparison_time_experiment():
    L = 20 # Кількість прогонів або згенерованих ІЗ для одного значення n
    H = 22 # Кількість смужок, після якої АПП не буде використовуватися

    # Параметри алгоритмів
    N = 20000 # Загальна кількість ітерацій для АВП

    K = 30 # кількість поколінь або ітерацій ГА
    I = 40 # розмір популяції для ГА
    b = 1/2 # частка особин, обраних для схрещення у ГА
    t = 3 # кількість особин, що беруть участь у кожному турнірі ГА
    mp = 0.01 # вірогідність мутації біту у векторі рішень в ГА

    n_stripes_array = [5,10,15,20,25,30,35] #,40,45,50]

    T_greedy = [None for _ in range(len(n_stripes_array))]
    T_random = [None for _ in range(len(n_stripes_array))]
    T_genetic = [None for _ in range(len(n_stripes_array))]
    T_BFS = [None for _ in range(len(n_stripes_array))]
    
    for i, n_stripes in enumerate(n_stripes_array):
        print(f"Iteration {i} | {n_stripes} stripes")
        t_greedy = 0
        t_random = 0
        t_genetic = 0
        t_BFS = 0
        for j in range(L):
            print(f"Run {j}")
            P_matrix = StripesConstructor.generate_random_P_matrix(n_stripes)

            _, _, t = track_time(greedy_maximum_non_overlapping_rectangles, P_matrix)
            t_greedy += t
            
            _, _, t = track_time(random_search, n_stripes, P_matrix, N)
            t_random += t

            _, _, t = track_time(genetic_algorithm, P_matrix, I, K, mp)
            t_genetic += t

            if n_stripes <= H:
                _, _, t = track_time(bfs_search, P_matrix)
                t_BFS += t

        T_greedy[i] = t_greedy / L
        T_random[i] = t_random / L
        T_genetic[i] = t_genetic / L
        if n_stripes <= H:
            T_BFS[i] = t_BFS / L

    # Побудова графіків
    algos_Ts = [T_greedy, T_random, T_genetic, T_BFS]
    algos_names = ["Greedy", "Random search", "Genetic", "BFS"]
    color_map = ["red", "green", "blue", "orange"]
    
    _, axes = plt.subplots(1, len(algos_Ts), figsize=(15, len(algos_Ts)))
    for i, algo_T in enumerate(algos_Ts):
        axes[i].plot(n_stripes_array, algo_T)
        axes[i].set_title(algos_names[i])
        axes[i].set_xticks(n_stripes_array) 
        axes[i].set_xlabel('Number of stripes')
        axes[i].set_ylabel('Time Consumed')
        axes[i].grid(True)
    plt.savefig('src/results/comparison_time_experiment_4_graphics.png')
    plt.show()

    _, axes = plt.subplots(1, 2, figsize=(15, 6))
    for i in range(2):
        if i == 1:
            algos_Ts.remove(T_BFS)
            algos_names.remove("BFS")
        for j, algo_T in enumerate(algos_Ts):
            axes[i].plot(n_stripes_array, algo_T, marker='o', color=color_map[j], label=algos_names[j])
        axes[i].set_xticks(n_stripes_array)
        axes[i].set_xlabel('Number of stripes')
        axes[i].set_ylabel('Time Consumed')
        axes[i].set_title('Time Consumed vs Number of stripes')
        axes[i].grid(True)
        axes[i].legend()
    plt.savefig('src/results/comparison_time_experiment_2_graphics.png')
    plt.show()


def comparison_precise_experiment():
    L = 20 # Кількість прогонів або згенерованих ІЗ для одного значення n
    H = 22 # Кількість прогонів, після якої АПП не буде використовуватися

    # Параметри алгоритмів
    N = 20000 # Загальна кількість ітерацій для АВП

    K = 30 # кількість поколінь або ітерацій ГА
    I = 40 # розмір популяції для ГА
    b = 1/2 # частка особин, обраних для схрещення у ГА
    t = 3 # кількість особин, що беруть участь у кожному турнірі ГА
    mp = 0.01 # вірогідність мутації біту у векторі рішень в ГА

    n_stripes_array = [5,10,15,20,25,30,35,40,45,50]

    avg_deviations_greedy = [None for _ in range(len(n_stripes_array))]
    avg_deviations_random = [None for _ in range(len(n_stripes_array))]
    avg_deviations_genetic = [None for _ in range(len(n_stripes_array))]
    avg_deviations_BFS = [None for _ in range(len(n_stripes_array))]

    for i, n_stripes in enumerate(n_stripes_array):
        print(f"Iteration {i} | {n_stripes} stripes")
        sum_deviations_greedy = 0
        sum_deviations_random = 0
        sum_deviations_genetic = 0
        sum_deviations_BFS = 0
        for j in range(L):
            print(f"Run {j}")
            P_matrix, known_F = StripesConstructor.generate_P_matrix_with_known_F(n_stripes)
            # print("known F", known_F)

            _, F = greedy_maximum_non_overlapping_rectangles(P_matrix)
            deviation = abs(F - known_F) / known_F
            sum_deviations_greedy += deviation
            
            _, F = random_search(n_stripes, P_matrix, N)
            deviation = abs(F - known_F) / known_F
            sum_deviations_random += deviation

            _, F = genetic_algorithm(P_matrix, I, K, mp)
            deviation = abs(F - known_F) / known_F
            sum_deviations_genetic += deviation

            if n_stripes <= H:
                _, F = bfs_search(P_matrix)
                # print(F)
                deviation = abs(F - known_F) / known_F
                sum_deviations_BFS += deviation

        avg_deviations_greedy[i] = sum_deviations_greedy / L
        avg_deviations_random[i] = sum_deviations_random / L
        avg_deviations_genetic[i] = sum_deviations_genetic / L
        if n_stripes <= H:
            avg_deviations_BFS[i] = sum_deviations_BFS / L

    # Побудова графіків
    algos_Ts = [avg_deviations_greedy, avg_deviations_random, avg_deviations_genetic, avg_deviations_BFS]
    algos_names = ["Greedy", "Random search", "Genetic", "BFS"]
    color_map = ["red", "green", "blue", "orange"]
    
    _, axes = plt.subplots(1, len(algos_Ts), figsize=(15, len(algos_Ts)))
    for i, algo_T in enumerate(algos_Ts):
        axes[i].plot(n_stripes_array, algo_T)
        axes[i].set_title(algos_names[i])
        axes[i].set_xticks(n_stripes_array) 
        axes[i].set_xlabel('Number of stripes')
        axes[i].set_ylabel('Average Deviation')
        axes[i].grid(True)
    plt.savefig('src/results/comparison_precise_experiment_4_graphics.png')
    plt.show()

    for j, algo_T in enumerate(algos_Ts):
        plt.plot(n_stripes_array, algo_T, marker='o', color=color_map[j], label=algos_names[j])
    plt.xticks(n_stripes_array)
    plt.xlabel('Number of stripes')
    plt.ylabel('Average Deviation')
    plt.title('Average Deviation vs Number of stripes')
    plt.grid(True)
    plt.legend()
    plt.savefig('src/results/comparison_precise_experiment_1_graphic.png')
    plt.show()