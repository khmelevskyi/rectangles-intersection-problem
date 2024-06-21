# def bfs_search(P):
#     n = len(P)
    
#     def is_valid_subset(subset):
#         for i in range(n):
#             for j in range(i+1, n):
#                 if subset[i] == 1 and subset[j] == 1 and P[i][j] == 1:
#                     return False
#         return True
    
#     max_stripes = 0
#     best_subset = None
    
#     for i in range(2**n):

#         binary_str = bin(i)[2:].zfill(n) # remove '0b' prefix and fill the binary with zeros
#         subset = [int(bit) for bit in binary_str]
#         if is_valid_subset(subset):
#             num_stripes = sum(subset)
#             if num_stripes > max_stripes:
#                 max_stripes = num_stripes
#                 best_subset = subset
    
#     return best_subset, max_stripes

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
    
    return best_subset, max_stripes


