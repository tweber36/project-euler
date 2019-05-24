from pyler import EulerProblem


class Problem0016(EulerProblem):
    """
    215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26. What is the
    sum of the digits of the number 21000?
    """

    problem_id = 16
    simple_input = 15
    simple_output = 26
    real_input = 1000
    real_output = 1366

    @staticmethod
    def solver(input_val):
        return sum(map(int, str(2 ** input_val)))

    @staticmethod
    def solver2(input_val):
        return sum(int(digit) for digit in str(2 ** input_val))

    @staticmethod
    def solver3(input_val):
        def sum_digits(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        return sum_digits(2 ** input_val)

    @staticmethod
    def solver4(input_val):
        def sum_digits(n):
            s = 0
            while n:
                n, remainder = divmod(n, 10)
                s += remainder
            return s

        return sum_digits(2 ** input_val)

    @staticmethod
    def solver5(input_val):
        def sum_digits(n):
            r = 0
            while n:
                r, n = r + n % 10, n // 10
            return r

        return sum_digits(2 ** input_val)


if __name__ == "__main__":
    import unittest

    unittest.main()
