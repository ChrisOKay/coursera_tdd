import unittest
from compute_stats_refactor import Stats

class TestStats(unittest.TestCase):

    def setUp(self) -> None:
        self.stats = Stats()

    def test_read_ints(self):
        numbers = self.stats.read_ints()
        self.assertGreater(numbers[0], 0)

    def test_count(self):
        self.assertGreater(self.stats.count(), 100)

    def test_summation(self):
        self.assertGreater(self.stats.summation(),  100)

    def test_average(self):
        self.assertGreater(self.stats.average(),  100)

    def test_minimum(self):
        self.assertLess(self.stats.minimum(),  self.stats.average())

    def test_maximum(self):
        self.assertGreater(self.stats.maximum(),  self.stats.average())

    def test_harmonic_mean(self):
        self.assertGreater(self.stats.harmonic_mean(), 100)

    def test_variance_mean(self):
        self.assertGreater(self.stats.variance(), 100)

    def test_standard_dev(self):
        self.assertGreater(self.stats.standard_dev(), 100)