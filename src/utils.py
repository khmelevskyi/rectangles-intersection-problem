import time


def track_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    # print(f"Execution time: {elapsed_time:.2f} seconds")
    if result is not None:
        return *result, elapsed_time
    else:
        return elapsed_time