import random
import statistics
import sys
import time
from typing import Callable


class Chromosome:
    genes = None
    fitness = None

    def __init__(self, genes, fitness):
        self.genes = genes
        self.fitness = fitness


class Benchmark:
    @staticmethod
    def run(function: Callable):
        timings = []
        stdout = sys.stdout
        for i in range(100):
            sys.stdout = None
            start_time = time.time()
            function()
            seconds = time.time() - start_time
            sys.stdout = stdout
            timings.append(seconds)
            mean = statistics.mean(timings)
            if i< 10 or i%10 == 9:
                print("{0} {1:3.2f} {2:3.2f}".format(
                    1 + i, mean, statistics.stdev(timings, mean) if i > 1 else 0
                ))


def _generate_parent(length: int, gene_set: str, get_fitness: Callable) -> Chromosome:
    genes = []
    while len(genes) < length:
        sample_size = min(length - len(genes), len(gene_set))
        genes.extend(random.sample(gene_set, sample_size))
    genes = ''.join(genes)
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)


def _mutate(parent: Chromosome, gene_set: str, get_fitness: Callable) -> Chromosome:
    index = random.randrange(0, len(parent.genes))
    child_genes = list(parent.genes)
    new_gene, alternate = random.sample(gene_set, 2)
    child_genes[index] = alternate if new_gene == child_genes[index] else new_gene
    genes = ''.join(child_genes)
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)


def get_best(get_fitness: Callable, target_len: int, optimal_fitness: int, gene_set: str,
             display: Callable) -> Chromosome:
    random.seed()
    best_parent = _generate_parent(target_len, gene_set, get_fitness)
    display(best_parent)

    if best_parent.fitness >= optimal_fitness:
        return best_parent

    while True:
        child = _mutate(best_parent, gene_set, get_fitness)
        if best_parent.fitness >= child.fitness:
            continue
        display(child)
        if child.fitness >= optimal_fitness:
            return child
        best_parent = child
