from pyler import EulerProblem


class Problem0613(EulerProblem):
    """
    Dave is doing his homework on the balcony and, preparing a presentation
    about Pythagorean triangles, has just cut out a triangle with side lengths
    30cm, 40cm and 50cm from some cardboard, when a gust of wind blows the
    triangle down into the garden. Another gust blows a small ant straight onto
    this triangle. The poor ant is completely disoriented and starts to crawl
    straight ahead in random direction in order to get back into the grass.
    Assuming that all possible positions of the ant within the triangle and all
    possible directions of moving on are equiprobable, what is the probability
    that the ant leaves the triangle along its longest side? Give your answer
    rounded to 10 digits after the decimal point.
    """
    problem_id = 613
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

