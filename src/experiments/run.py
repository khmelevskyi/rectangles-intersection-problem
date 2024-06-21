from src.utils import track_time
from src.experiments.bfs_exp import bfs_experiment
from src.experiments.genetic_exp import genetic_algo_experiment
from src.experiments.random_search_exp import random_search_experiment
from src.experiments.comparison_exps import comparison_precise_experiment,\
                                            comparison_time_experiment


def run_experiments():
    exp_choice = input( "\n"\
                        "1 - Random search experiment\n"\
                        "2 - Genetic algorithm experiment\n"\
                        "3 - BFS experiment\n"\
                        "4 - Comparison experiment (time)\n"\
                        "5 - Comparison experiment (precise/deviation)\n"\
                        "0 - Exit\n"\
                        "-----\n"\
                        "Your choice: ")
    
    # 1st experiment - Random search
    if exp_choice == "1":
        random_search_experiment()
    
    elif exp_choice == "2":
        # 2nd experiment - Genetic algo
        genetic_algo_experiment()

    elif exp_choice == "3":
        #3rd experiment - BFS algo
        bfs_experiment()
    
    elif exp_choice == "4":
        # 4th experiment - General (time)
        total_consumed_time = track_time(comparison_time_experiment)
        print(f"Total consumed time for the comparison time experiment: {int(total_consumed_time)} seconds")

    elif exp_choice == "5":
        # 5th experiment - General (precise/deviation)
        total_consumed_time = track_time(comparison_precise_experiment)
        print(f"Total consumed time for the comparison precise (deviation) experiment: {int(total_consumed_time)} seconds")
    
    elif exp_choice == '0':
        print("Exiting...")
        exit()

    else:
        print("Invalid choice. Please try again.")
