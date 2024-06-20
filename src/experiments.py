import numpy as np
import matplotlib.pyplot as plt

from src.random_search_algo import random_search_for_experiment, random_search
from src.tasks_generator import StripesConstructor


def random_search_experiment(n_stripes, N, L):
    BF = {}  # Массив для збереження кращих значень ЦФ
    iterations = {}

    for i in range(L):
        BF[i] = []
        iterations[i] = []

        P_matrix, known_F = StripesConstructor.generate_P_matrix_with_known_F(n_stripes)
        print(known_F)
        for j in range(1000, N, 10000):
            # Виклик функції random_search()
            best_solution, best_value = random_search(n_stripes, P_matrix, j)

            BF[i].append(best_value)
            iterations[i].append(j)

    # Побудова графіків
    fig, axes = plt.subplots(1, L, figsize=(15, L))
    fig.tight_layout(pad=3.0)

    for i in range(L):
        axes[i].plot(iterations[i], BF[i])
        axes[i].set_title(f'Run {i+1}')
        axes[i].set_xlabel('Iterations')
        axes[i].set_ylabel('Best Value')
        axes[i].legend()

    plt.savefig('src/results/random_search_experiment_results.png')
    plt.show()

    return BF

def run_experiments():
    # 1st experiment - Random search
    n_stripes = 20  # розмірність задачі (кількість смуг)
    N = 200000  # Загальна кількість ітерацій
    L = 5  # кількість прогонів для одного значення N або кількість ІЗ

    BF = random_search_experiment(n_stripes, N, L)