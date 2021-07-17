from pyler.pyler import EulerProblem


class Problem0031(EulerProblem):
    """
    In the United Kingdom the currency is made up of pound (£) and pence (p).
    There are eight coins in general circulation: 1p, 2p, 5p, 10p, 20p, 50p, £1
    (100p), and £2 (200p). It is possible to make £2 in the following way: 1×£1
    + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p How many different ways can £2 be made
    using any number of coins?
    """
    problem_id = 31
    simple_input = 200
    simple_output = 73682
    real_input = 200
    real_output = 73682

    @staticmethod
    def solver(input_val):
        coins = [1, 2, 5, 10, 20, 50, 100, 200]

        def ways(target, pos_highest_coin):
            if pos_highest_coin <= 1:
                return 1
            count = 0
            while target >= 0:
                count += ways(target, pos_highest_coin - 1)
                target -= coins[pos_highest_coin - 1]
            return count

        return ways(input_val, len(coins))

    @staticmethod
    def solver2(input_val):
        coins = [1, 2, 5, 10, 20, 50, 100, 200]
        memoization = {}

        def ways(target, pos_highest_coin):
            if pos_highest_coin <= 1:
                return 1
            t = target
            if memoization.get((t, pos_highest_coin), 0) > 0:
                return memoization[(t, pos_highest_coin)]
            count = 0
            while target >= 0:
                count += ways(target, pos_highest_coin - 1)
                target -= coins[pos_highest_coin - 1]
            memoization[(t, pos_highest_coin)] = count
            return count

        return ways(input_val, len(coins))

    @staticmethod
    def solver3(input_val):
        coins = [1, 2, 5, 10, 20, 50, 100, 200]
        ways = {0: 1}
        for i in range(len(coins)):
            for j in range(coins[i], input_val + 1):
                ways[j] = ways.get(j, 0) + ways.get(j - coins[i], 0)
        return ways[input_val]


if __name__ == '__main__':
    import unittest
    unittest.main()

