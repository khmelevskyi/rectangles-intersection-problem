from collections import deque

def bfs_search(P):
    n = len(P)
    
    # Ініціалізація BFS черги з пустою підмножиною
    queue = deque([[]])
    
    max_stripes = 0
    best_subset = []

    while queue:
        current_subset = queue.popleft()
        
        # Перевірка, чи є поточна підмножина валідною
        def is_valid_subset(subset):
            for i in range(len(subset)):
                for j in range(i + 1, len(subset)):
                    if P[subset[i]][subset[j]] == 1:
                        return False
            return True

        if is_valid_subset(current_subset):
            num_stripes = len(current_subset)
            if num_stripes > max_stripes:
                max_stripes = num_stripes
                best_subset = current_subset
        
        # Генерація нових підмножин, додаючи кожен індекс смуги
        start_index = current_subset[-1] + 1 if current_subset else 0
        for i in range(start_index, n):
            new_subset = current_subset + [i]
            queue.append(new_subset)
    
    # Створення бінарного вектора X
    X = [0] * n
    for idx in best_subset:
        X[idx] = 1

    return X, max_stripes


