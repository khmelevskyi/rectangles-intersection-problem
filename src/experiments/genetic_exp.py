import matplotlib.pyplot as plt
import numpy as np

from src.tasks_generator import StripesConstructor
from src.algos import genetic_algorithm


def genetic_algo_experiment():
    L = 10 # Кількість прогонів або згенерованих ІЗ для одного значення n
    n_stripes = 30 # Кількість смужок

    K = 30 # кількість поколінь або ітерацій ГА
    b = 1/2 # частка особин, обраних для схрещення у ГА
    t = 3 # кількість особин, що беруть участь у кожному турнірі ГА
    mp = 0.01 # вірогідність мутації біту у векторі рішень в ГА

    I_values = [I for I in range(4, 162, 4)] # розміри популяцій

    avg_deviations_genetic = [None for _ in range(len(I_values))]

    for i, pop_size in enumerate(I_values):
        print(f"Iteration {i} | {pop_size} population size")
        sum_deviations_genetic = 0
        for j in range(L):
            print(f"Run {j}")
            P_matrix, known_F = StripesConstructor.generate_P_matrix_with_known_F(n_stripes)
   
            _, F = genetic_algorithm(P_matrix, pop_size, K, mp)
            deviation = abs(F - known_F) / known_F
            sum_deviations_genetic += deviation

        avg_deviations_genetic[i] = sum_deviations_genetic / L

    # Побудова графіків
    #calculate equation for quadratic trendline
    z = np.polyfit(I_values, avg_deviations_genetic, 2)
    p = np.poly1d(z)

    plt.figure().set_figwidth(15)
    plt.plot(I_values, avg_deviations_genetic, marker='o', label="Avg Deviation")
    plt.plot(I_values, p(I_values), linestyle='--', label='Quadratic Trendline')
    plt.xticks(I_values)
    plt.xlabel('I (Population Size)')
    plt.ylabel('Avg Deviation')
    plt.title('Avg Deviation vs. I')
    plt.grid(True)
    plt.legend()
    plt.savefig('src/results/genetic_algo_experiment.png')
    plt.show()