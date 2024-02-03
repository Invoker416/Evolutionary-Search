# Genetic Algorithms in Python

This repository contains Python implementations of genetic algorithms for solving different problems, showcasing concepts in evolutionary computation. The code is structured into three main scripts, each addressing a unique problem domain.

## Code Structure Description

### Deceptive Landscape.py

This script implements a genetic algorithm for the Deceptive Landscape problem. The algorithm challenges the genetic optimization process by using a deceptive fitness function, which disproportionately rewards strings with no 1s. Key components include:

- `generate_initial_population`: Creates an initial population of random binary strings.
- `fitness_deceptive`: A modified fitness function that rewards strings with no 1s disproportionately.
- `select`, `crossover`, `mutate`: Functions for genetic algorithm operations (selection, crossover, mutation).
- `main`: Orchestrates the genetic algorithm, running it for a set number of generations and plotting the average fitness over time.

### One-Max & Target-String.py

This script includes implementations for the One-Max problem and evolving towards a target string. It demonstrates how different fitness functions can influence genetic algorithms. The main differences from Deceptive Landscape.py are in the fitness functions:

- `fitness_one_max`: Counts the number of 1s in a string for the One-Max problem.
- `fitness_target_string`: Compares the string to a target sequence for the Target String problem.

Similar to the Deceptive Landscape, this script plots the average fitness of the population over generations, providing visual insights into the algorithm's performance.

### Bin-Pack.py

This script implements a genetic algorithm for the Bin Packing problem, focusing on efficiently packing items into the fewest bins possible without exceeding each bin's capacity. The key components of this implementation include:

- `generate_initial_population`: Generates an initial population where solutions randomly assign items to bins, ensuring no bin's capacity is exceeded.
- `fitness_bin_packing`: Evaluates a solution based on the total number of bins used, aiming to minimize this value.
- `select_bin_packing`, `crossover_bin_packing`, `mutate_bin_packing`: Adapted genetic algorithm operations for the bin packing problem representation and constraints.
- `main_bin_packing`: Orchestrates the genetic algorithm, focusing on minimizing the number of bins used and plotting the average fitness over generations.

Each script showcases a different aspect of evolutionary computation, from deceptive landscapes and simple optimization to solving complex combinatorial problems like bin packing. The implementations provide a foundation for exploring and analyzing the effectiveness of genetic algorithms across various problem domains.
