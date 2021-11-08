import random


def _generate_parent(length, gene_set):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(gene_set))
        genes.extend(random.sample(gene_set, sampleSize))
    return ''.join(genes)


def _mutate(parent, gene_set):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(gene_set, 2)
    childGenes[index] = alternate if newGene == childGenes[index] else newGene
    return ''.join(childGenes)


def get_best(get_fitness, target_len, optimal_fitness, gene_set, display):
    random.seed()
    bestParent = _generate_parent(target_len, gene_set)
    bestFitness = get_fitness(bestParent)
    display(bestParent)

    if bestFitness >= optimal_fitness:
        return bestParent

    while True:
        child = _mutate(bestParent, gene_set)
        childFitness = get_fitness(child)
        if bestFitness >= childFitness:
            continue
        display(child)
        if childFitness >= optimal_fitness:
            return child
        bestFitness = childFitness
        bestParent = child
