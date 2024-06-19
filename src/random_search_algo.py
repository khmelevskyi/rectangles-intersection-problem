import numpy as np

from src.utils import track_time


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

@track_time
def random_search(n, P, N, iteration_callback):
    """Алгоритм випадкового пошуку"""
    best_solution = None
    best_f = 0
    
    for _ in range(N):
        iteration_callback() # track iteration function from track_time

        x = generate_random_solution(n)
        if is_valid_solution(x, P):
            f = evaluate_solution(x)
            if f > best_f:
                best_solution = x
                best_f = f
                
    return best_solution, best_f

