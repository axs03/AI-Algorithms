# Genetic Algorithm
A genetic algorithm (GA) is an optimization and search heuristic inspired by the process of natural selection and genetics. It works by 
iteratively evolving a population of candidate solutions to a problem, using operators such as selection, crossover (recombination), and mutation.

## Python Pseudo Code
```python
def genetic_algorithm(problem, f_thres, n_gen=1000):
    # Initialize the population
    population = problem.init_population()

    # Check if we generated the solution based on the random generation
    best = problem.fittest(population, f_thres)
    if best: 
        return -1, best

    # Iterate through generations
    for i in range(n_gen):
        population = problem.next_generation(population)
        best = problem.fittest(population, f_thres)
        if best: 
            return i, best

    # Else, the chromosome with fitness value better than f_thres has not been found
    # Still return the fittest individual even though its fitness is worse than f_thres
    best = problem.fittest(population)
    return n_gen, best</code>
```
## How it Works
### Initialize
This step creates an initial population randomly

### Selection
Select the fittest individuals from the current population to serve as parents for the next generation. Common methods include roulette wheel selection, tournament selection, or rank-based selection.

### Crossover (Recombination):
Combine pairs of parent solutions to produce offspring by exchanging genetic material, simulating biological reproduction. This introduces new combinations of traits.

### Mutation:
Introduce small random changes to some individuals in the population to maintain genetic diversity and avoid premature convergence.

### Replacement:
Form the next generation by replacing the least fit individuals with the newly created offspring.

### Iteration:
Repeat the evaluation, selection, crossover, mutation, and replacement steps for multiple generations.

### Termination:
Stop the process when a predefined condition is met, such as reaching a maximum number of generations, achieving a satisfactory fitness level, or observing no significant improvement.
