import random
import operator
import math
from deap import base, creator, tools

# Define the symbolic regression equation: y = ax^2 - bx + c
def symbolic_regression_equation(x, a, b, c):
    return a * x**2 - b * x + c

# Define the evaluation function.
def eval_func(individual, points):
    a, b, c = individual
    error = 0.0
    for x, y in points:
        error += abs(symbolic_regression_equation(x, a, b, c) - y)
    return error,

# Create the toolbox with the right parameters.
def create_toolbox():
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)
    toolbox = base.Toolbox()
    toolbox.register("attr_float", random.uniform, -10, 10)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=3)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", eval_func, points=[(i, symbolic_regression_equation(i, 2, 3, -5)) for i in range(-10, 11)])
    toolbox.register("mate", tools.cxBlend, alpha=0.5)  # Blend crossover
    toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.1)  # Gaussian mutation
    toolbox.register("select", tools.selTournament, tournsize=3)
    return toolbox

if __name__ == "__main__":
    toolbox = create_toolbox()
    random.seed(7)
    population = toolbox.population(n=500)
    probab_crossing, probab_mutating = 0.5, 0.2
    num_generations = 50
    print("\nSymbolic Regression with Genetic Algorithm starts")

    # Evaluate the entire population.
    fitnesses = list(map(toolbox.evaluate, population))
    for ind, fit in zip(population, fitnesses):
        ind.fitness.values = fit
    print("Evaluated", len(population), "individuals")

    # Create and iterate through generations.
    for g in range(num_generations):
        print("\n- Generation", g)

        # Select the next generation individuals.
        offspring = toolbox.select(population, len(population))

        # Clone the selected individuals.
        offspring = list(map(toolbox.clone, offspring))

        # Apply crossover and mutation on the offspring.
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < probab_crossing:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < probab_mutating:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Evaluate the individuals with an invalid fitness.
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = list(map(toolbox.evaluate, invalid_ind))
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        print('Evaluated', len(invalid_ind), 'individuals')

        # Replace population with the next generation individuals.
        population[:] = offspring

        # Print the statistics for the current generation.
        fits = [ind.fitness.values[0] for ind in population]
        length = len(population)
        mean = sum(fits) / length
        sum2 = sum(x*x for x in fits)
        std = abs(sum2 / length - mean**2)**0.5
        print('Min:', min(fits), ', Max:', max(fits))
        print('Average:', round(mean, 2), ', Standard deviation:', round(std, 2))
    print("\n- Evolution ends")

    # Print the best individual.
    best_ind = tools.selBest(population, 1)[0]
    print('\nBest individual:', best_ind)
    a, b, c = best_ind
    print('Best parameters: a={}, b={}, c={}'.format(a, b, c))
