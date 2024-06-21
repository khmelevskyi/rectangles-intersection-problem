import matplotlib.pyplot as plt

from src.utils import track_time
from src.tasks_generator import StripesConstructor
from src.algos import bfs_search


def bfs_experiment():
    L = 20 # Кількість прогонів або згенерованих ІЗ для одного значення n
    n_stripes = 18
    
    percentages_array = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9] # m – частка одиниць у P 

    T_BFS = [None for _ in range(len(percentages_array))]
    
    for i, m in enumerate(percentages_array):
        print(f"Iteration {i} | {m}% of 1s in P_matrix")
        t_BFS = 0
        for j in range(L):
            print(f"Run {j}")
            P_matrix = StripesConstructor.generate_random_P_with_percentage(n_stripes, m)

            _, _, t = track_time(bfs_search, P_matrix)
            t_BFS += t

        T_BFS[i] = t_BFS / L

    # Побудова графіків    
    plt.figure().set_figwidth(15)
    plt.plot(percentages_array, T_BFS, marker='o', label="Avg Time Consumed")
    plt.xticks(percentages_array)
    plt.xlabel('% of 1s in P matrix')
    plt.ylabel('Time Consumed')
    plt.title('Time Consumed vs % of 1s in P matrix')
    plt.grid(True)
    plt.legend()
    plt.savefig('src/results/bfs_algo_experiment.png')
    plt.show()