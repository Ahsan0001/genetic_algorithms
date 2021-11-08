import datetime
import random
import unittest

from make_password_guess import display, get_fitness
import genetic


class GuessPasswordTests(unittest.TestCase):
    gene_set = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."

    def test_Hello_World(self):
        target = "Hello World!"
        self.guess_password(target)

    def test_For_I_am_fearfully_and_wondefully_made(self):
        target = "For I am fearfully and wonderfullt made."
        self.guess_password(target)

    def test_random(self):
        length = 150
        target = ''.join(random.choice(self.gene_set) for _ in range(length))
        self.guess_password(target)

    def test_benchmark(self):
        genetic.Benchmark.run(self.test_random)

    def guess_password(self, target):
        start_time = datetime.datetime.now()

        def fn_get_fitness(genes):
            return get_fitness(genes, target)

        def fn_display(candidate):
            display(candidate, start_time)

        optimalFitness = len(target)
        best = genetic.get_best(fn_get_fitness, len(target), optimalFitness, self.gene_set, fn_display)
        self.assertEqual(best.genes, target)


if __name__ == "__main__":
    unittest.main()
