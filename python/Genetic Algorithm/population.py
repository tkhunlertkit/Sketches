class Population(object):

    tournament_size = 5

    def __init__(self, number, gene_length, gene_type=None, target = None):
        self.population = []
        if gene_type:
            for i in range(number):
                self.population.append(gene_type(gene_length))

        self.target = target
        self.evaluate_flag = False

    def evaluate(self):
        self.population = sorted(self.population, key=lambda x: x.fitness(self.target), reverse = True)
        self.evaluate_flag = True

    def evolve(self):
        if not self.evaluate_flag:
            self.evaluate()


    def select(self):
        
