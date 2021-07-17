import unittest
from timeit import Timer

from .utils import convert_time


class EulerProblem(unittest.TestCase):

    problem_id = None

    simple_input = None
    simple_output = None
    real_input = None
    real_output = None

    @staticmethod
    def solver(input_val):
        raise NotImplementedError()

    @classmethod
    def setUpClass(cls):
        if cls.solver is EulerProblem.solver:
            raise unittest.SkipTest(
                "Not running the tests for a not implemented problem"
            )

    def test_simple(self):
        """
        Checks the simple example for all implemented solutions
        """
        solutions = [func for func in dir(self) if func.startswith("solver")]
        for func in solutions:
            self.assertEqual(getattr(self, func)(self.simple_input), self.simple_output)

    def test_real(self):
        """
        Checks all implemented solutions give the right answer
        """
        solutions = [
            getattr(self, func)(self.real_input)
            for func in dir(self)
            if func.startswith("solver")
        ]
        for solution in solutions:
            self.assertEqual(solution, self.real_output)

    def test_time(self):
        """
        Measure the response time of each implementation
        """
        solutions = [func for func in dir(self) if func.startswith("solver")]
        timings = {}
        for solver in solutions:
            t = Timer(
                f"p.{solver}(p.real_input)",
                setup=f"from solutions.problem_{self.problem_id:04d} import Problem{self.problem_id:04d};"
                f"p=Problem{self.problem_id:04d}()",
            )
            results = t.autorange()
            timings[solver] = results[1] / results[0]
            self.assertTrue(timings[solver] < 60)
        for solver, timing in timings.items():
            print(f"Average time for {solver}: {convert_time(timing)}")
