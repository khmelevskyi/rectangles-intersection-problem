import matplotlib.pyplot as plt

from src.tasks_generator import StripesConstructor
from src.algos import genetic_algorithm


def genetic_algo_experiment():
    n = 50 
    P, F = StripesConstructor.generate_P_matrix_with_known_F(n)
    #print_matrix(P) 
    print("optimum: ",F) 
    pop_size = 100 
    generations = 10 
    mutation_rate = 0.01 
    
    I_values = range(4, 412, 4) 
    
    best_fitnesses = []
    
    for I in I_values: 
        best_solution, best_fitness = genetic_algorithm(P, I, generations, mutation_rate) 
        best_fitnesses.append(best_fitness)
    
    # Plotting the results 
    plt.figure().set_figwidth(20) 
    plt.plot(I_values, best_fitnesses, marker='o') 
    #plt.xticks(I_values) 
    plt.yticks(best_fitnesses) 
    plt.xlabel('I (Population Size)') 
    plt.ylabel('Best Solution (Fitness)') 
    plt.title('Best Solution vs. I') 
    plt.grid(True) 
    plt.show()