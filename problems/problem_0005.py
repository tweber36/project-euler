from collections import Counter
from functools import reduce
from math import floor, log
from pyler import EulerProblem
from utils import prime_factors, primes_list


class Problem0005(EulerProblem):
    """
    2520 is the smallest number that can be divided by each of the numbers from
    1 to 10 without any remainder. What is the smallest positive number that is
    evenly divisible by all of the numbers from 1 to 20?
    """
    problem_id = 5
    simple_input = 10
    simple_output = 2520
    real_input = 20
    real_output = 232792560
    
    @staticmethod
    def solver(input_val):
        lcm = 1  # Least common multiple
        for p in primes_list(input_val):
            if p > input_val:
                break

            if p > input_val ** 0.5:
                p_power = 1
            else:
                p_power = floor(log(input_val) / log(p))
            lcm *= p ** p_power
        return lcm

    @staticmethod
    def solver2(input_val):
        factors = [Counter(prime_factors(x)) for x in range(2, input_val + 1)]
        factors_min = {}
        for p in factors:
            for prime, power in p.items():
                if prime not in factors_min:
                    factors_min[prime] = power
                elif power > factors_min[prime]:
                    factors_min[prime] = power

        return reduce(lambda x, key: x * pow(key, factors_min[key]), factors_min, 1)

if __name__ == '__main__':
    import unittest
    unittest.main()

