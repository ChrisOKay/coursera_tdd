
class Stats:

    def __init__(self, file='random_nums.txt'):
        self.file = file

    @property
    def numbers(self):
        try:
            return self._numbers
        except AttributeError:
            with open(self.file, 'r') as file:
                self._numbers = [int(number) for number in file]
            return self._numbers

    def read_ints(self):
        """Reads in the data from random_nums.txt and convert them into a list of integers"""
        return self.numbers

    def count(self):
        """Returns the total number of elements in random_nums.txt"""
        return len(self.read_ints())

    def summation(self):
        """Returns the sum of all of the elements in random_nums.txt"""
        return sum(self.read_ints())

    def average(self):
        """Returns the average of all of the elements in random_nums.txt"""
        return self.summation() / self.count()

    def minimum(self):
        """Returns the smallest integer in random_nums.txt"""
        return min(self.numbers)

    def maximum(self):
        """Returns the largest integer in random_nums.txt"""
        return max(self.numbers)

    def harmonic_mean(self):
        """Returns the harmonic mean of the elements in random_nums.txt"""
        return self.count() / sum(1/number for number in self.numbers)

    def variance(self):
        """Returns the variance of the elements in random_nums.txt"""
        return 1 / self.count() * sum((number-self.average())**2 for number in self.numbers)

    def standard_dev(self):
        """Returns the standard deviation of all of the elements in random_nums.txt"""
        return self.variance()**0.5

if __name__ == '__main__':
    stats = Stats('random_nums.txt')

    print(f'total = {stats.count()}')
    print(f'summation = {stats.summation()}')
    print(f'average = {stats.average()}')
    print(f'Minimum = {stats.minimum()}')
    print(f'Maximum = {stats.maximum()}')
