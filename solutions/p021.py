import unittest

from pyler.pyler import EulerProblem
from utils.misc import sum_of_proper_divisors
from utils.prime_generator import rwh_primes


class Problem0021(EulerProblem, unittest.TestCase):
    """
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n
    which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a
    and b are an amicable pair and each of a and b are called amicable numbers.
    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
    55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
    71 and 142; so d(284) = 220. Evaluate the sum of all the amicable numbers
    under 10000.
    """

    problem_id = 21
    simple_input = 10000
    simple_output = 31626
    real_input = 10000
    real_output = 31626

    @staticmethod
    def sum_of_divisors(n):
        """ Slow but short solution to get the sum of divisors of a number n """
        return sum(d for d in range(1, n // 2 + 1) if n % d == 0)

    @staticmethod
    def sum_of_divisors2(n):
        """
        Fast solution using the prime decomposition of n
        https://mathschallenge.net/index.php?section=faq&ref=number/sum_of_divisors
        """
        if n == 1:
            return 1
        n_temp = n
        primes = rwh_primes(int(n ** 0.5))
        answer = 1
        for p in primes:
            if p * p > n_temp or n_temp <= 1:
                break
            if n_temp % p == 0:
                prime_factor = 1
                n_temp //= p
                while n_temp % p == 0:
                    prime_factor += 1
                    n_temp //= p
                answer *= (p ** (prime_factor + 1) - 1) // (p - 1)
        if n_temp > 1:
            answer *= n_temp + 1
        return answer - n

    @staticmethod
    def sum_of_amicable(input_val, func):
        """
        Faster because we compute func only twice (compared to 3 times in the
        previous solution)
        """
        answer = 0
        for a in range(2, input_val):
            b = func(a)
            if b > a:
                if func(b) == a:
                    answer += a + b
        return answer

    def solver(self, input_val):
        return self.sum_of_amicable(input_val, self.sum_of_divisors)

    def solver2(self, input_val):
        return self.sum_of_amicable(input_val, self.sum_of_divisors2)

    def solver3(self, input_val):
        return self.sum_of_amicable(input_val, sum_of_proper_divisors)


if __name__ == "__main__":
    unittest.main()
