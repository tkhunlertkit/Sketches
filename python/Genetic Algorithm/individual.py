import random
import string

class Individual(object):

    mutation_threshold = 0.3
    breed_threshold    = 0.5
    selection = string.letters[:26]

    def __init__(self, length, start = None):
        self.gene = []

        if not start:
            for i in range(length):
                self.gene.append(random.choice(Individual.selection))
        else:
            for i in start:
                self.gene.append(i)

    def mutate(self):
        res = Individual(0, self.gene)
        for i in range(len(res.gene)):
            if random.random() < Individual.mutation_threshold:
                res.gene[i] = random.choice(random.choice(Individual.selection))

        return res

    def breed(self, other):
        if not isinstance(other, Individual):
            print '[!] Breeding with non-individual'
            exit()

        mi = min(len(self.gene), len(other.gene))
        ma = max(len(self.gene), len(other.gene))

        offspring = Individual(len(self.gene))

        for i in range(mi):
            offspring.gene[i] = self.gene[i] if random.random() < Individual.breed_threshold else other.gene[i]

        if mi < ma:
            offspring.gene[mi:] = (self.gene[mi:] if len(self.gene) > len(other.gene) else other.gene[mi:])

        return offspring

    def fitness(self, target):
        error = 0
        for i, j in zip(self.gene, target.gene):
            val_i = Individual.selection.index(i)
            val_j = Individual.selection.index(j)
            error += abs(val_j - val_i)

        return -error

    def __str__(self):
        return ''.join(self.gene)
