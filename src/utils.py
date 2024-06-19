import time


def track_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        iteration_count = [0]  # Use a list to mutate the count within the callback

        def iteration_callback():
            iteration_count[0] += 1
            if iteration_count[0] % 1_000_000 == 0:
                print(f"Iteration: {iteration_count[0]}")

        result = func(*args, iteration_callback=iteration_callback, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Execution time: {elapsed_time:.2f} seconds")
        return result
    return wrapper