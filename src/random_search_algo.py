import numpy as np

from src.tasks_generator import StripesConstructor

def generate_random_solution(n):
    """Генерація випадкового вектора розмірності n, де кожен елемент може бути 0 або 1"""
    return np.random.randint(2, size=n)

def is_valid_solution(x, P):
    """Перевірка допустимості розв'язку x відносно матриці пересічності P"""
    n = len(x)
    for i in range(n):
        if x[i] == 1:
            for j in range(n):
                if i != j and x[j] == 1 and P[i][j] == 1:
                    return False
    return True

def evaluate_solution(x):
    """Обчислення кількості одиниць у векторі x"""
    return np.sum(x)

def random_search(n, P, N):
    """Алгоритм випадкового пошуку"""
    best_solution = None
    best_f = 0
    
    for _ in range(N):

        x = generate_random_solution(n)
        if is_valid_solution(x, P):
            f = evaluate_solution(x)
            if f > best_f:
                best_solution = x
                best_f = f
                
    return best_solution, best_f

def random_search_for_experiment(n, P):
    x = generate_random_solution(n)
    if is_valid_solution(x, P):
        f = evaluate_solution(x)
    else:
        f = None
    return f



if __name__ == "__main__":
    n_stripes = 10  # розмірність задачі (кількість смуг)
    N = 20000  # Загальна кількість ітерацій
    P_matrix = StripesConstructor.generate_random_P_matrix(n_stripes)
    bs, bf = random_search(n_stripes, P_matrix, N)
    print(bf)