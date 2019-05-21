from pyler import EulerProblem


class Problem0332(EulerProblem):
    """
    A spherical triangle is a figure formed on the surface of a sphere by three
    great circular arcs intersecting pairwise in three vertices.  Let C(r) be
    the sphere with the centre (0,0,0) and radius r. Let Z(r) be the set of
    points on the surface of C(r) with integer coordinates. Let T(r) be the set
    of spherical triangles with vertices in Z(r). Degenerate spherical
    triangles, formed by three points on the same great arc, are not included in
    T(r). Let A(r) be the area of the smallest spherical triangle in T(r). For
    example A(14) is 3.294040 rounded to six decimal places. Find $\sum
    \limits_{r = 1}^{50} {A(r)}$. Give your answer rounded to six decimal
    places.
    """
    problem_id = 332
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

