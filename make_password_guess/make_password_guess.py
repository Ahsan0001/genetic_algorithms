import datetime

from genetic import Chromosome


def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes) if expected == actual)


def display(candidate: Chromosome, start_time: datetime):
    time_diff = datetime.datetime.now() - start_time
    print("{0}\t{1}\t{2}".format(candidate.genes, candidate.fitness, str(time_diff)))


