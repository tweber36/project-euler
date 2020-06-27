import unittest

from pyler.pyler import EulerProblem
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
        Faster solution that uses the two facts:
        1. for every divisor d, n / d is also a divisor (they come by pair except
         for a perfect square)
        2. Odd numbers cannot have even divisors
        """
        if n == 1:
            return 1
        limit = int(n ** 0.5)
        if limit * limit == n:
            answer = 1 + limit
            limit -= 1
        else:
            answer = 1
        divisor_ini, step = (3, 2) if (n & 1) else (2, 1)
        answer += sum(
            divisor + n // divisor
            for divisor in range(divisor_ini, limit + 1, step)
            if n % divisor == 0
        )
        return answer

    @staticmethod
    def sum_of_divisors3(n):
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
        """ Slow but short solution """
        return sum(
            i for i in range(1, input_val + 1) if (func(func(i)) == i and i != func(i))
        )

    @staticmethod
    def sum_of_amicable2(input_val, func):
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
        return self.sum_of_amicable(input_val, self.sum_of_divisors3)

    def solver4(self, input_val):
        return self.sum_of_amicable2(input_val, self.sum_of_divisors)

    def solver5(self, input_val):
        return self.sum_of_amicable2(input_val, self.sum_of_divisors2)

    def solver6(self, input_val):
        return self.sum_of_amicable2(input_val, self.sum_of_divisors3)


if __name__ == "__main__":
    unittest.main()
