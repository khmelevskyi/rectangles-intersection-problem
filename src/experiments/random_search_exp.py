import matplotlib.pyplot as plt

from src.tasks_generator import StripesConstructor
from src.algos import random_search_for_experiment


def random_search_experiment(n_stripes, N, L):
    BF = {}  # Массив для збереження кращих значень ЦФ
    iterations = {}

    for i in range(L):
        BF[i] = []
        iterations[i] = []

        P_matrix, known_F = StripesConstructor.generate_P_matrix_with_known_F(n_stripes)
        print(known_F)
        best_value = 0
        for j in range(N):
            # Виклик функції random_search()
            current_value = random_search_for_experiment(n_stripes, P_matrix)

            if current_value is not None and current_value > best_value:
                best_value = current_value
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

    plt.grid(True)
    plt.show()
    plt.savefig('src/results/random_search_experiment_results.png')

    return BF