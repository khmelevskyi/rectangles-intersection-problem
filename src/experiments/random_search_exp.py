import matplotlib.pyplot as plt

from src.tasks_generator import StripesConstructor
from src.algos import random_search_for_experiment


def random_search_experiment():
    n_stripes = 25  # розмірність задачі (кількість смуг)
    N = 200000  # Загальна кількість ітерацій
    L = 5  # кількість прогонів для одного значення N або кількість ІЗ
    
    BF = {}  # Массив для збереження кращих значень ЦФ
    iterations = {}

    for i in range(L):
        BF[i] = []
        iterations[i] = []

        P_matrix = StripesConstructor.generate_random_P_matrix(n_stripes)
        # print(known_F)
        best_value = 0
        for j in range(N):
            # Виклик функції random_search()
            current_value = random_search_for_experiment(n_stripes, P_matrix)

            if current_value is not None and current_value > best_value:
                best_value = current_value
            BF[i].append(best_value)
            iterations[i].append(j)

    # Побудова графіків
    _, axes = plt.subplots(1, L, figsize=(15, L))
    for i in range(L):
        axes[i].plot(iterations[i], BF[i])
        axes[i].set_title(f'Run {i+1}')
        axes[i].set_xlabel('Iterations')
        axes[i].set_ylabel('Best Value')
        axes[i].grid(True)

    plt.savefig('src/results/random_search_experiment.png')
    plt.show()

    return BF