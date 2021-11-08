import datetime
import unittest

import genetic


def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes) if expected == actual)


def display(genes, target, start_time):
    timeDiff = datetime.datetime.now() - start_time
    fitness = get_fitness(genes, target)
    print("{0}\t{1}\t{2}".format(genes, fitness, str(timeDiff)))


class GuessPasswordTests(unittest.TestCase):
    geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."

    def test_Hello_World(self):
        target = "Hello World!"
        self.guess_password(target)

    def test_For_I_am_fearfully_and_wondefully_made(self):
        target = "For I am fearfully and wonderfullt made."
        self.guess_password(target)

    def guess_password(self, target):
        startTime = datetime.datetime.now()

        def fn_get_fitness(genes):
            return get_fitness(genes, target)

        def fn_display(genes):
            display(genes, target, startTime)

        optimalFitness = len(target)
        best = genetic.get_best(fn_get_fitness, len(target), optimalFitness, self.geneSet, fn_display)
        self.assertEqual(best, target)


if __name__ == "__main__":
    unittest.main()
