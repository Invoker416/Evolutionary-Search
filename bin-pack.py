import random
import matplotlib.pyplot as plt


def read_bpp_instances(file_path):
    instances = []
    with open(file_path, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break  # End of file
            line = line.strip()
            if 'BPP' in line:
                # Start of a new problem instance
                instance = {'name': line, 'items': []}
                m = int(file.readline().strip())  # Number of different item weights
                C = int(file.readline().strip())  # Capacity of bins
                instance['m'] = m
                instance['C'] = C
                for _ in range(m):
                    item_line = file.readline().strip()
                    weight, count = map(int, item_line.split())
                    instance['items'].append({'weight': weight, 'count': count})
                instances.append(instance)
    return instances

# Usage example
file_path = 'D:\\Download\\Binpacking.txt'
bpp_instances = read_bpp_instances(file_path)

# Displaying the first few instances to verify the function's output
for instance in bpp_instances[:1]:  # Displaying the first two instances for brevity
    print(instance)


def generate_initial_population(problem_instance, pop_size):
    population = []
    num_bins = len(problem_instance['items'])
    for _ in range(pop_size):
        solution = [-1] * num_bins  # -1 indicates that the item is not yet placed
        for i, item in enumerate(problem_instance['items']):
            while True:
                bin_index = random.randint(0, num_bins - 1)
                if can_place_item(solution, problem_instance, bin_index, item):
                    solution[i] = bin_index
                    break
        population.append(solution)
    return population

def can_place_item(solution, problem_instance, bin_index, item):
    total_weight = sum(problem_instance['items'][i]['weight'] * problem_instance['items'][i]['count']
                       for i in range(len(solution)) if solution[i] == bin_index)
    return total_weight + item['weight'] * item['count'] <= problem_instance['C']

def fitness_bin_packing(solution, problem_instance):
    return len(set(solution))  # Number of bins used

def select_bin_packing(population, tournament_size, problem_instance):
    selected = []
    while len(selected) < len(population):
        tournament = random.sample(population, tournament_size)
        winner = min(tournament, key=lambda x: fitness_bin_packing(x, problem_instance))
        selected.append(winner)
    return selected

def crossover_bin_packing(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    return offspring1, offspring2

def mutate_bin_packing(individual, problem_instance):
    item_index = random.randint(0, len(individual) - 1)
    new_bin = random.randint(0, len(individual) - 1)
    individual[item_index] = new_bin
    return individual

def main_bin_packing(problem_instance):
    pop_size = 100
    mutation_rate = 0.01
    crossover_rate = 0.7
    generations = 100
    tournament_size = 3

    population = generate_initial_population(problem_instance, pop_size)
    average_fitness_history = []

    for gen in range(generations):
        selected = select_bin_packing(population, tournament_size, problem_instance)
        new_population = []

        while len(new_population) < pop_size:
            parent1, parent2 = random.sample(selected, 2)
            if random.random() < crossover_rate:
                offspring1, offspring2 = crossover_bin_packing(parent1, parent2)
            else:
                offspring1, offspring2 = parent1, parent2

            offspring1 = mutate_bin_packing(offspring1, problem_instance)
            offspring2 = mutate_bin_packing(offspring2, problem_instance)

            new_population.extend([offspring1, offspring2])

        population = new_population[:pop_size]

        # Calculate and output average fitness
        average_fitness = sum(fitness_bin_packing(individual, problem_instance) for individual in population) / pop_size
        average_fitness_history.append(average_fitness)

    # Plotting
    plt.plot(range(generations), average_fitness_history)
    plt.xlabel('Generation')
    plt.ylabel('Average Fitness')
    plt.title('Average Fitness over Generations in Bin Packing Problem')
    plt.show()

# Example usage with the first problem instance from bpp_instances
main_bin_packing(bpp_instances[0])
main_bin_packing(bpp_instances[1])
main_bin_packing(bpp_instances[2])

