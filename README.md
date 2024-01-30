# Genetic Algorithms in Python
This repository contains Python implementations of genetic algorithms for demonstrating various evolutionary computation concepts.

# Code Structure Description

This repository contains Python implementations of genetic algorithms for solving different problems, showcasing concepts in evolutionary computation. The code is structured into two main scripts:

1. **Deceptive Landscape.py**: This script implements a genetic algorithm for the Deceptive Landscape problem. The algorithm challenges the genetic optimization process by using a deceptive fitness function. The key components of the code include:
   - `generate_initial_population`: Creates an initial population of random binary strings.
   - `fitness_deceptive`: A modified fitness function that rewards strings with no 1s disproportionately.
   - `select`, `crossover`, `mutate`: Functions for genetic algorithm operations (selection, crossover, mutation).
   - `main`: The main function orchestrates the genetic algorithm, running it for a set number of generations and plotting the average fitness over time.

2. **One-Max&target-string.py**: This script includes implementations for the One-Max problem and evolving towards a target string. It demonstrates how different fitness functions can be used in genetic algorithms. The code structure is similar to `Deceptive Landscape.py`, with the main differences being in the fitness functions:
   - `fitness_one_max`: Counts the number of 1s in a string for the One-Max problem.
   - `fitness_target_string`: Compares the string to a target sequence for the Target String problem.

Both scripts use a similar approach for the genetic algorithm, allowing for comparison and analysis of different problem types within the evolutionary computation domain. Each script plots the average fitness of the population over generations, providing visual insights into the algorithm's performance.
