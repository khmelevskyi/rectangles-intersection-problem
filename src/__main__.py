from pprint import pprint

from src.experiments import run_experiments
from src.tasks_generator import StripesConstructor
from src.algos import greedy_maximum_non_overlapping_rectangles,\
                      random_search, genetic_algorithm,\
                      bfs_search


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
            if len(rect) == 4:
                rectangles[i] = rect
                i += 1
            else:
                print("Invalid input. Please enter the coordinates in the correct format and ensure each rectangle has exactly 4 corners.")
                break
    return rectangles

def run_algorithms(P_matrix):
    print()
    # BFS algo
    print("BFS Algorithm:")
    X, F = bfs_search(P_matrix)
    print("Best solution, X vector:", X)
    print("Maximum number of non-overlapping stripes, F:", F)
    print()

    # Greedy algorithm
    print("Greedy Algorithm:")
    X, F = greedy_maximum_non_overlapping_rectangles(P_matrix)
    print("Best solution, X vector:", X)
    print("Maximum number of non-overlapping stripes, F:", F)
    print()

    # Random search
    n = len(P_matrix)  # number of stripes
    N = 10000  # number of iterations
    print("Random Search Algorithm:")
    X, F = random_search(n, P_matrix, N)
    print("Best solution, X vector:", X)
    print("Maximum number of non-overlapping stripes, F:", F)
    print()

    # Genetic algorithm
    n = len(P_matrix)  # number of stripes
    pop_size = 100  # population size
    N = 100 # number of generations
    print("Genetic Algorithm:")
    X, F = genetic_algorithm(P_matrix, pop_size, N)
    print("Best solution, X vector:", X)
    print("Maximum number of non-overlapping stripes, F:", F)
    print()


def main():
    print("Main Menu:")
    while True:
        choice = input( "\n"\
                        "1 - Input rectangles manually\n"\
                        "2 - Generate random rectangles\n"\
                        "3 - Display the conditions of the task\n"\
                        "4 - Run all algorithms\n"\
                        "5 - Run experiments\n"\
                        "0 - Exit\n"\
                        "-----\n"\
                        "Your choice: ")

        if choice == '1': # manual input
            input_manually_choice_2 = input("\n"\
                                            "1 - Input rectangles manually in terminal\n"\
                                            "2 - Read rectangle coordinates from the file\n"\
                                            "0 - Exit\n"\
                                            "-----\n"\
                                            "Your choice: ")
            if input_manually_choice_2 == "1":
                rectangles = input_rectangles_manually()
            elif input_manually_choice_2 == "2":
                file_path = input("Input the file name (skip for default = 'input_rectangles.txt'): ") or "input_rectangles.txt"
                rectangles = read_rectangles_from_file("src/data/" + file_path)
            elif input_manually_choice_2 == '0':
                print("Exiting...")
                exit()
            else:
                print("Invalid choice. Please try again.")
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
            stripes_constructor.generate_random_rectangles()
            P_matrix = stripes_constructor.construct_P_matrix()
        
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
            run_experiments()

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
