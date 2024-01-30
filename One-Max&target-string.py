import random
import matplotlib.pyplot as plt

def generate_initial_population(pop_size, string_length):
    # Generate initial population
    population = []
    for _ in range(pop_size):
        individual = ''.join(random.choice('01') for _ in range(string_length))
        population.append(individual)
    return population

def fitness_one_max(individual):
    # Calculate fitness for the One-max problem
    return individual.count('1')

def fitness_target_string(individual, target_string):
    # Calculate fitness for the target string problem
    return sum(individual[i] == target_string[i] for i in range(len(individual)))

def select(population, tournament_size, fitness_function, additional_params=None):
    # Selection process
    selected = []
    while len(selected) < len(population):
        tournament = random.sample(population, tournament_size)
        winner = max(tournament, key=lambda x: fitness_function(x, **(additional_params or {})))
        selected.append(winner)
    return selected

def crossover(parent1, parent2):
    # One-point crossover
    crossover_point = random.randint(1, len(parent1) - 1)
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    return offspring1, offspring2

def mutate(individual, mutation_rate):
    # Mutation process
    mutated_individual = ""
    for bit in individual:
        if random.random() < mutation_rate:
            mutated_individual += '1' if bit == '0' else '0'
        else:
            mutated_individual += bit
    return mutated_individual

def run_genetic_algorithm(fitness_function, string_length, pop_size, mutation_rate, crossover_rate, generations, tournament_size, additional_params=None):
    population = generate_initial_population(pop_size, string_length)
    average_fitness_history = []

    for gen in range(generations):
        selected = select(population, tournament_size, fitness_function, additional_params)
        new_population = []

        while len(new_population) < pop_size:
            parent1, parent2 = random.sample(selected, 2)
            if random.random() < crossover_rate:
                offspring1, offspring2 = crossover(parent1, parent2)
            else:
                offspring1, offspring2 = parent1, parent2

            offspring1 = mutate(offspring1, mutation_rate)
            offspring2 = mutate(offspring2, mutation_rate)

            new_population.extend([offspring1, offspring2])

        population = new_population[:pop_size]  # Ensure population size remains constant

        # Calculate and output average fitness
        average_fitness = sum(fitness_function(individual, **(additional_params or {})) for individual in population) / pop_size
        average_fitness_history.append(average_fitness)

    # Plotting
    plt.plot(range(generations), average_fitness_history)
    plt.xlabel('Generation')
    plt.ylabel('Average Fitness')
    plt.title('Average Fitness over Generations')
    plt.show()

def main():
    string_length = 30
    pop_size = 100
    mutation_rate = 0.01
    crossover_rate = 0.7
    generations = 100
    tournament_size = 3  # Define the tournament size for selection

    # Run genetic algorithm for One-max problem
    print("Running One-max problem")
    run_genetic_algorithm(fitness_one_max, string_length, pop_size, mutation_rate, crossover_rate, generations, tournament_size)

    # Run genetic algorithm for Evolving to a Target String problem
    print("\nRunning Evolving to a Target String problem")
    target_string = "101010101010101010101010101010"  # Example target string
    run_genetic_algorithm(fitness_target_string, string_length, pop_size, mutation_rate, crossover_rate, generations, tournament_size, additional_params={'target_string': target_string})

main()
