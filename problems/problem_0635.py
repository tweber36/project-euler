from pyler import EulerProblem


class Problem0635(EulerProblem):
    """
    Let $A_q(n)$ be the number of subsets, $B$, of the set $\{1, 2, ..., q \cdot
    n\}$ that satisfy two conditions: 1) $B$ has exactly $n$ elements; 2) the
    sum of the elements of $B$ is divisible by $n$.   E.g. $A_2(5)=52$ and
    $A_3(5)=603$.  Let $S_q(L)$ be $\sum A_q(p)$ where the sum is taken over all
    primes $p \le L$. E.g. $S_2(10)=554$, $S_2(100)$ mod
    $1\,000\,000\,009=100433628$ and $S_3(100)$ mod
    $1\,000\,000\,009=855618282$.   Find $S_2(10^8)+S_3(10^8)$. Give your answer
    modulo $1\,000\,000\,009$.
    """
    problem_id = 635
    simple_input = 0
    simple_output = 1
    real_input = 0
    real_output = 1
    
    @staticmethod
    def solver(input_val):
        raise NotImplementedError


if __name__ == '__main__':
    import unittest
    unittest.main()

