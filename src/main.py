from pprint import pprint
from src.tasks_generator import StripesConstructor
from src.random_search_algo import random_search
from src.greedy_algo import greedy_maximum_non_overlapping_rectangles
from src.brute_force_algo import brute_force_algo


def input_rectangles_manually():
    """
    Function to input rectangle coordinates manually.

    This function prompts the user for the number of rectangles and their coordinates.
    The coordinates are entered in a string format for each rectangle, and then the
    function returns these rectangles.
    """
    n = int(input("Enter the number of rectangles (skip for default = 9): ") or 9)
    rectangles = {}
    for i in range(n):
        while True:
            rect_str = input(f"Enter the coordinates for rectangle {i+1} in the format (x1,y1), (x2,y2), (x3,y3), (x4,y4): ").strip()
            rect = [tuple(map(int, point.strip().strip('()').split(','))) for point in rect_str.split('), (')]
            print(rect)
            if len(rect) == 4:
                rectangles[i] = rect
                break
            else:
                print("Invalid input. Please enter the coordinates in the correct format and ensure each rectangle has exactly 4 corners.")

    return rectangles

def read_rectangles_from_file(file_path):
    """
    Reads rectangle coordinates from a file and returns them as a dict of rectangles.

    Args:
        file_path (str): The path to the file containing rectangle coordinates.
    """
    rectangles = {}
    with open(file_path, 'r') as file:
        i = 0
        for line in file:
            rect_str = line.strip()
            rect = [tuple(map(int, point.strip().strip('()').split(','))) for point in rect_str.split('), (')]
            rectangles[i] = rect
            i += 1
    return rectangles

def run_algorithms(P_matrix):
    print()
    # Greedy algorithm
    print("Greedy Algorithm:")
    X, F = greedy_maximum_non_overlapping_rectangles(P_matrix)
    print("Best solution, X vector:", X)
    print("Maximum number of non-overlapping stripes, F:", F)
    print()

    # Random search
    n = len(P_matrix)  # number of stripes
    N = 100000  # number of iterations
    print("Random Search Algorithm:")
    X, F = random_search(n, P_matrix, N)
    print("Best solution, X vector:", X)
    print("Maximum number of non-overlapping stripes, F:", F)
    print()

    # Brute force
    print("Brute Force Algorithm:")
    X, F = brute_force_algo(P_matrix)
    print("Best solution, X vector:", X)
    print("Maximum number of non-overlapping stripes, F:", F)
    print()

def generate_and_run_experiments(num_experiments, n_stripes, max_x, max_y):
    for i in range(num_experiments):
        print(f"Experiment {i+1}:")
        stripes_constructor = StripesConstructor(n_stripes, max_x, max_y)
        rectangles, P_matrix = stripes_constructor.generate_rects_and_P_matrix()
        stripes_constructor.visualize_rectangles()
        run_algorithms(P_matrix)

def main():
    print("Main Menu:")
    while True:
        choice = input( "\n"\
                        "1 - Input rectangles manually\n"\
                        "2 - Generate random rectangles\n"\
                        "3 - Display the conditions of the task\n"\
                        "4 - Run all algorithms\n"\
                        "5 - Run experiments with multiple StripeConstructors\n"\
                        "0 - Exit\n"\
                        "-----\n"\
                        "Your choice: ")

        if choice == '1': # manual input
            input_manually_choice_2 = input("\n"\
                                            "1 - Input rectangles manually in terminal\n"\
                                            "2 - Read rectangle coordinates from the file\n"\
                                            "-----\n"\
                                            "Your choice: ")
            if input_manually_choice_2 == "1":
                rectangles = input_rectangles_manually()
            else:
                file_path = input("Input the file name (skip for default = 'input_rectangles.txt'): ") or "input_rectangles.txt"
                rectangles = read_rectangles_from_file("src/data/" + file_path)
            n = len(rectangles)
            print(rectangles.items())
            max_x = max(max(rect, key=lambda x: x[0])[0] for rect in rectangles.values())
            max_y = max(max(rect, key=lambda x: x[1])[1] for rect in rectangles.values())
            stripes_constructor = StripesConstructor(n, max_x, max_y, rectangles)
            P_matrix = stripes_constructor.construct_P_matrix()

        elif choice == '2': # random generation
            n = int(input("Enter the number of rectangles (skip for default = 9): ") or 9)
            max_x = int(input("Enter the maximum x value (skip for default = 100): ") or 100)
            max_y = int(input("Enter the maximum y value (skip for default = 100): ") or 100)
            stripes_constructor = StripesConstructor(n, max_x, max_y)
            P_matrix = stripes_constructor.generate_indiv_task(mode="full")
        
        elif choice == '3': # display
            if 'stripes_constructor' in locals():
                print("\nNumber of stripes:", stripes_constructor.number_of_stripes)
                print("The rectangles:\n", stripes_constructor.rectangles)
                print("The P matrix:")
                pprint(stripes_constructor.P_matrix, width=100)
                stripes_constructor.visualize_rectangles()
            else:
                print("No rectangles have been generated or input yet. Please input or generate rectangles first.")

        elif choice == '4': # demonstration of algorithms
            if 'stripes_constructor' in locals():
                run_algorithms(P_matrix)
            else:
                print("No rectangles have been generated or input yet. Please input or generate rectangles first.")

        elif choice == '5': # experiments
            num_experiments = int(input("Enter the number of experiments: "))
            n_stripes = int(input("Enter the number of rectangles for each experiment: "))
            max_x = int(input("Enter the maximum x value: "))
            max_y = int(input("Enter the maximum y value: "))
            generate_and_run_experiments(num_experiments, n_stripes, max_x, max_y)

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
