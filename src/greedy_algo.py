import numpy as np

from src.utils import track_time


@track_time
def greedy_maximum_non_overlapping_rectangles(P, iteration_callback):
    n = len(P)
    X = [0] * n  # This will be our solution vector

    # Compute the number of overlaps for each rectangle
    overlaps = [(sum(P[i]), i) for i in range(n)]

    # Sort rectangles by the number of overlaps (increasing)
    overlaps.sort() # n*logn

    for _, i in overlaps:
        iteration_callback() # track iteration function from track_time

        # Check if adding this rectangle would cause any conflict
        can_add = True
        for j in range(n):
            if i != j and X[j] == 1 and P[i][j] == 1:
                can_add = False
                break

        if can_add:
            X[i] = 1

    return X, np.sum(X)
# n2 * logn

