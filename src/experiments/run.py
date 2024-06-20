from src.utils import track_time
from src.experiments.genetic_exp import genetic_algo_experiment
from src.experiments.random_search_exp import random_search_experiment
from src.experiments.comparison_exps import comparison_precise_experiment,\
                                            comparison_time_experiment
    

def run_experiments():
    # 1st experiment - Random search
    n_stripes = 20  # розмірність задачі (кількість смуг)
    N = 20000  # Загальна кількість ітерацій
    L = 5  # кількість прогонів для одного значення N або кількість ІЗ

    # BF = random_search_experiment(n_stripes, N, L)

    # 2nd experiment - Genetic algo
    # genetic_algo_experiment()

    # 3rd experiment - General (time)
    total_consumed_time = track_time(comparison_time_experiment)
    print(f"Total consumed time for the comparison experiment: {total_consumed_time}")
