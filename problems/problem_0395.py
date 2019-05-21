from pyler import EulerProblem


class Problem0395(EulerProblem):
    """
    The Pythagorean tree is a fractal generated by the following procedure:
    Start with a unit square. Then, calling one of the sides its base (in the
    animation, the bottom side is the base):  Attach a right triangle to the
    side opposite the base, with the hypotenuse coinciding with that side and
    with the sides in a 3-4-5 ratio. Note that the smaller side of the triangle
    must be on the 'right' side with respect to the base (see animation).
    Attach a square to each leg of the right triangle, with one of its sides
    coinciding with that leg.  Repeat this procedure for both squares,
    considering as their bases the sides touching the triangle.  The resulting
    figure, after an infinite number of iterations, is the Pythagorean tree.
    It can be shown that there exists at least one rectangle, whose sides are
    parallel to the largest square of the Pythagorean tree, which encloses the
    Pythagorean tree completely.   Find the smallest area possible for such a
    bounding rectangle, and give your answer rounded to 10 decimal places.
    """
    problem_id = 395
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
