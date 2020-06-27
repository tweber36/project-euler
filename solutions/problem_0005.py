from collections import Counter
from functools import reduce
from math import log

from pyler.pyler import EulerProblem
from utils.prime_generator import rwh_primes
from utils.primes import prime_factors


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
        """
        Let p[i] be the i th prime number: p[1] = 2, p[2] = 3, p[3] = 5, … .
        Let N = p[1]^a[1] * p[2]^a[2] * p[3]^a[3] * … ;
        initially, let a[i] = 0 for all i.
        For j = 2 to k, write each j in the form, p[1]^b[1] * p[2]^b[2] * p[3]^b[3] * …
        and set a[i] = max(a[i], b[i]).

        However, this approach requires a function to be constructed to express a
        given number as a product of prime factors.
        """
        factors = [Counter(prime_factors(x)) for x in range(2, input_val + 1)]
        factors_min = {}
        for p in factors:
            for prime, power in p.items():
                if prime not in factors_min:
                    factors_min[prime] = power
                elif power > factors_min[prime]:
                    factors_min[prime] = power

        return reduce(lambda x, key: x * pow(key, factors_min[key]), factors_min, 1)

    @staticmethod
    def solver2(input_val):
        """
        Same idea as solver but faster for small values of input_val.
        But as input_val grows (more than a few hundreds), this becomes slower than
        solver.
        """
        lcm = 1
        for k in range(1, input_val + 1):
            if lcm % k > 0:
                for j in range(1, input_val + 1):
                    if (lcm * j) % k == 0:
                        lcm *= j
                        break
        return lcm

    @staticmethod
    def solver3(input_val):
        """
        we want the LCM of 1 through N. Clearly, we only need a list of all primes ≤N,
        and for each prime, we need its maximum possible power that won't exceed N
        (remember that the LCM must be able to "contain" up to the maximum prime power
        of all prime factors among all the numbers included in the LCM function).
        Finding the maximum power can be done with logarithms.
        """
        lcm = 1  # Least common multiple
        for p in rwh_primes(input_val):
            if p > input_val ** 0.5:
                p_power = 1
            else:
                p_power = int(log(input_val) / log(p))
            lcm *= p ** p_power
        return lcm


if __name__ == "__main__":
    import unittest
    unittest.main()
