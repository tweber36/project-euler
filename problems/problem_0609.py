from pyler import EulerProblem


class Problem0609(EulerProblem):
    """
    For every $n \ge 1$ the prime-counting function $\pi(n)$ is equal to the
    number of primes not exceeding $n$. E.g. $\pi(6)=3$ and $\pi(100)=25$.   We
    say that a sequence of integers $u  = (u_0,\cdots,u_m)$ is a $\pi$ sequence
    if   $u_n \ge 1$ for every $n$  $u_{n+1}= \pi(u_n)$  $u$ has two or more
    elements  For $u_0=10$ there are three distinct $\pi$ sequences: (10,4),
    (10,4,2) and (10,4,2,1).   Let  $c(u)$ be the number of elements of $u$ that
    are not prime. Let $p(n,k)$ be the number of $\pi$ sequences $u$  for which
    $u_0\le n$ and $c(u)=k$. Let $P(n)$ be the product of all $p(n,k)$ that are
    larger than 0. You are given: P(10)=3×8×9×3=648 and P(100)=31038676032.
    Find $P(10^8)$. Give your answer modulo 1000000007.
    """
    problem_id = 609
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

