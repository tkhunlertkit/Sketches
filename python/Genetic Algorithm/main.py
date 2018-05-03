from individual import Individual
from population import Population
import string

GENE_LENGTH = 5

if __name__ == '__main__':

    target = Individual(0, 'aaaaa')
    population = Population(20, GENE_LENGTH, Individual, target)
    population.evaluate()

    for p in population.population:
        print p, p.fitness(target)
