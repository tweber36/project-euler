from pyler.pyler import EulerProblem


class Problem0014(EulerProblem):
    """
    The following iterative sequence is defined for the set of positive
    integers: n → n/2 (n is even)n → 3n + 1 (n is odd) Using the rule above and
    starting with 13, we generate the following sequence: 13 → 40 → 20 → 10 → 5
    → 16 → 8 → 4 → 2 → 1 It can be seen that this sequence (starting at 13 and
    finishing at 1) contains 10 terms. Although it has not been proved yet
    (Collatz Problem), it is thought that all starting numbers finish at 1.
    Which starting number, under one million, produces the longest chain? NOTE:
    Once the chain starts the terms are allowed to go above one million.
    """

    problem_id = 14
    simple_input = 13
    simple_output = 9
    real_input = 1000000
    real_output = 837799

    @staticmethod
    def solver(input_val):
        cache = {1: 1}
        longest_chain, answer = 0, -1

        for i in range(input_val // 2, input_val):
            value = i
            counter = 1

            while value != 1:
                if value in cache:
                    counter += cache[value]
                    break
                if value % 2 == 0:
                    counter += 1
                    value /= 2
                else:
                    counter += 2
                    value = (3 * value + 1) / 2

            cache[i] = counter

            if counter > longest_chain:
                longest_chain = counter
                answer = i
        return answer

    """ Slow methods
    @staticmethod
    def solver2(input_val):
        def collatz(n):
            return n // 2 if n % 2 == 0 else 3 * n + 1

        def distance(n, cache=None):
            if cache is None:
                cache = {1: 1}
            if n not in cache:
                cache[n] = distance(collatz(n)) + 1
            return cache[n]

        return max(range(1, input_val), key=distance)

    @staticmethod
    def solver3(input_val):
        longest_chain = 0
        answer = 0

        for i in range(1, input_val):
            collatz = [i]
            counter = 1

            while collatz[-1] != 1:
                if collatz[-1] % 2 == 0:
                    collatz.append(collatz[-1] / 2)
                else:
                    collatz.append(3 * collatz[-1] + 1)
                    counter += 1

            if counter > longest_chain:
                longest_chain = counter
                answer = i

        return answer
    """


if __name__ == "__main__":
    import unittest
    unittest.main()
