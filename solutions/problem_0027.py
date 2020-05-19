import unittest

from prime_generator import rwh_primes
from pyler import EulerProblem
from utils import is_prime2


class Problem0027(EulerProblem, unittest.TestCase):
    """
    Euler discovered the remarkable quadratic formula: $n^2 + n + 41$ It turns
    out that the formula will produce 40 primes for the consecutive integer
    values $0 \le n \le 39$. However, when $n = 40, 40^2 + 40 + 41 = 40(40 + 1)
    + 41$ is divisible by 41, and certainly when $n = 41, 41^2 + 41 + 41$ is
    clearly divisible by 41. The incredible formula $n^2 - 79n + 1601$ was
    discovered, which produces 80 primes for the consecutive values $0 \le n \le
    79$. The product of the coefficients, −79 and 1601, is −126479. Considering
    quadratics of the form:  $n^2 + an + b$, where $|a| < 1000$ and $|b| \le
    1000$where $|n|$ is the modulus/absolute value of $n$e.g. $|11| = 11$ and
    $|-4| = 4$  Find the product of the coefficients, $a$ and $b$, for the
    quadratic expression that produces the maximum number of primes for
    consecutive values of $n$, starting with $n = 0$.
    """

    problem_id = 27
    simple_input = (1000, 1000)
    simple_output = -59231
    real_input = (1000, 1000)
    real_output = -59231

    def solver(self, input_val):
        def number_of_consecutive_primes(a, b):
            n = 0
            while is_prime2(n * n + a * n + b):
                n += 1
            return n

        primes_b = rwh_primes(input_val[1])
        max_number_primes = 0
        product = 0
        for b in primes_b:
            for a in range(-(b + 2), input_val[0] + 1):
                count = number_of_consecutive_primes(a, b)
                if count > max_number_primes:
                    max_number_primes = count
                    product = a * b
        return product

    def solver2(self, input_val):
        """
        When you research Euler's polynomial as stated in the problem, you will quickly
        come across:
        http://mathworld.wolfram.com/Prime-GeneratingPolynomial.html
        The "incredible" formula n^2−79n+1601 can be rewritten as
        (n−40)^2+(n−40)+41=k^2+k+41 where k=(n−40). In other words, it is another
        transformation of Euler's prime-generating polynomial. If p(n) generates
        primes for 0≤n≤L, then so does p(L−n).
        p(n)=n^2+n+41
        p(L−n)=(L−n)^2+(L−n)+41
        p(L−n)=n^2−2Ln−n+L^2+L+41
        p(L−n)=n^2−(2L+1)n+p(L)
        p(L−n)=n^2+an+b
        where a=−(2L+1) and b=L^2+L+41

        We also know that when n=0, p(0)=0^2+0a+b=b. Since p(n) needs to generate
        positive primes, this means b is a positive prime. According to the problem
        statement, we only care about b<1000. Therefore:

        b=L^2+L+41<1000⟹−31≤L≤30 in terms of integer solutions.

        We want the longest run of primes, which corresponds to the largest b possible
        here. Thus, we take L to be 30, which makes b equal to 30^2+30+41=971 and a
        equal to −(2(30)+1)=−61.

        Therefore:
        a=−61,b=971

        The answer is ab=(−61)(971)=−59231

        The following code solves for the maximum L value based on the limit you pass
        into the function, and returns the corresponding product of a and b.
        """
        L = int(0.5 * ((4 * input_val[1] - 163) ** 0.5 - 1))

        return (-(2 * L + 1)) * (L ** 2 + L + 41)


if __name__ == "__main__":
    unittest.main()
