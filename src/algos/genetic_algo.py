
import random


class UniqueRandom:
    def __init__(self, m, n):
        if m > n:
            raise ValueError("The starting value m must be less than or equal to the ending value n.")
        self.numbers = list(range(m, n + 1))  # List of numbers from m to n

    def get_unique_random(self):
        if not self.numbers:  # If the list is empty, return None
            return None
        num = random.choice(self.numbers)  # Choose a random number
        self.numbers.remove(num)  # Remove it from the list
        return num

    def get_simple_random(self):
        if not self.numbers:  # If the list is empty, return None
            return None
        num = random.choice(self.numbers)  # Choose a random number
        return num

    def get_simple_randoms(self, m):
        if not self.numbers:  # If the list is empty, return None
            return None
        nums = random.sample(self.numbers, m)  # Choose a random numbers
        return nums

    def get_unique_randoms(self, m):
        if not self.numbers:  # If the list is empty, return None
            return None
        nums = random.sample(self.numbers, m)  # Choose a random number
        for num in nums:
            self.numbers.remove(num) # Remove it from the list
        return nums

    def remove_option(self, num):
        self.numbers.remove(num);

def generateRandomP(n):
    P = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            P[i][j] = random.choice([0, 1])
            P[j][i] = P[i][j]
    return P

def fitness(X, P):
    if is_valid_solution(X, P):
        return sum(X)
    else:
        return 0

def is_valid_solution(X, P):
    for i in range(len(X)):
        for j in range(i + 1, len(X)):
            if X[i] + X[j] > 2 - P[i][j]:
                return False
    return True

def is_valid_partial_solution(X, P, index):
    for j in range(index):
        if X[index] + X[j] > 2 - P[index][j]:
            return False
    return True

def generate_valid_solution(n, P):
    X = [0]*n
    for i in range(n):
        X[i] = random.randint(0, 1)
        if not is_valid_partial_solution(X, P, i):
            X[i] = 1 - X[i]
    return X

def initialize_population(pop_size, n, P):
    population = []
    for _ in range(pop_size):
        X = generate_valid_solution(n, P)
        population.append(X)
    return population

def crossover(parent1, parent2, P):
    unique_random = UniqueRandom(0, len(parent1))
    point = unique_random.get_unique_random()

    while point is not None:
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        if is_valid_solution(child1, P) and is_valid_solution(child2, P):
            return child1, child2
        point = unique_random.get_unique_random()

    return parent1, parent2

def mutate(X, mutation_rate, P, max_iterations=1000):
    for _ in range(max_iterations):
        mutated = X.copy()
        for i in range(len(mutated)):
            if random.random() < mutation_rate:
                mutated[i] = 1 - mutated[i]

        if is_valid_solution(mutated, P):
            return mutated

    return X

def genetic_algorithm(P, pop_size=4, generations=1, mutation_rate=0.01):
    n = len(P)
    population = initialize_population(pop_size, n, P)
    #print("Initial length ", len(population))
    best_solution = None
    best_fitness = 0

    #print("Initial population", population);

    for generation in range(generations):
        #Calculation fitness
        fitness_values = [sum(X) for X in population]

        #Finding best solution
        max_fitness = max(fitness_values)
        if max_fitness > best_fitness:
            best_fitness = max_fitness
            best_solution = population[fitness_values.index(max_fitness)]

        #Tournament selection
        selected_parents = []
        selected_parents_indices = []
        unique_random = UniqueRandom(0, pop_size-1)
        for _ in range(pop_size // 2):
            tournament_indices = unique_random.get_simple_randoms(3);
            tournament = [population[i] for i in tournament_indices]
            tournament_fitness = [fitness_values[i] for i in tournament_indices]
            parent = tournament[tournament_fitness.index(max(tournament_fitness))]
            parent_index = tournament_indices[tournament.index(parent)]
            selected_parents_indices.append(parent_index)
            selected_parents.append(parent)
            try:
              unique_random.remove_option(parent_index)
              #print("No exception: unique random numbers ",unique_random.numbers, "removed ", parent_index)
            except:
              print("Exception: unique random numbers ",unique_random.numbers, "trying to remove ", parent_index)

        #Crossover and mutation
        new_population = []
        for i in range(0, len(selected_parents)-1, 2):
            try:
              parent1, parent2 = selected_parents[i], selected_parents[i+1]
            except:
              print("Exepiton: Selected parents length ", len(selected_parents), "Index i ",i, "Index i+1 ", i+1)
            child1, child2 = crossover(parent1, parent2, P)
            new_population.extend([mutate(child1, mutation_rate, P), mutate(child2, mutation_rate, P)])



        # Remove selected parents from population
        population = [item for index, item in enumerate(population) if index not in selected_parents_indices]

        #print("Population with removed parents ",population)

        # Add children obtained via crossover to population
        population.extend(new_population)

        #print("Popultation cycle end:")
        #print("Population length ", len(population))
        #print("Selected Parents", selected_parents)
        #print("Selected Children", new_population)
        #print("Selected Indices ", selected_parents_indices)
        #print("Updated population", population)
    return best_solution, best_fitness


#n = 30
#P = generateRandomP(n)

#best_solution, best_fitness = genetic_algorithm(P)
#print("Best solution:", best_solution)
#print("Maximum number of non-overlapping rectangles:", best_fitness)
