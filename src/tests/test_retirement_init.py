# CJ Nguyen
# 2/23/2021

# Tests the creation of RetirementCalculator Objects

import unittest

from ..classes.retirement import RetirementCalculator


class TestRetirementInit(unittest.TestCase):
    def setUp(self):
        """Setup function that will apply to all other functions in the class."""
        # Age that must be valid
        self.control_age = 30
        # Salary that must be valid
        self.control_salary = 80000
        # Salary percentage saved per year that must be valid
        self.control_spy = .12
        # Goal that must be valid
        self.control_goal = 700000

    def test_retirement_age_init(self):
        """Tests initializing the RetirementCalculator object at varying ages."""

        # Case: Age is -500
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.retirement_calculator = RetirementCalculator(-500, self.control_salary, self.control_spy,
                                                              self.control_goal)
        self.assertEqual(str(context.exception), "Age must be no less than 0 and no greater than 99 years.")

        # Case: Age is -1
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.retirement_calculator = RetirementCalculator(-1, self.control_salary, self.control_spy,
                                                              self.control_goal)
        self.assertEqual(str(context.exception), "Age must be no less than 0 and no greater than 99 years.")

        # Case: Age is 0 (boundary)
        # expected: pass
        self.retirement_calculator = RetirementCalculator(0, self.control_salary, self.control_spy,
                                                          self.control_goal)

        # Case: Age is 25
        # expected: pass
        self.retirement_calculator = RetirementCalculator(25, self.control_salary, self.control_spy,
                                                          self.control_goal)

        # Case: Age is 99 (boundary)
        # expected: pass
        self.retirement_calculator = RetirementCalculator(-1, self.control_salary, self.control_spy,
                                                          self.control_goal)

        # Case: Age is 100
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.retirement_calculator = RetirementCalculator(100, self.control_salary, self.control_spy,
                                                              self.control_goal)
        self.assertEqual(str(context.exception), "Age must be no less than 0 and no greater than 99 years.")

        # Case: Age is 500
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.retirement_calculator = RetirementCalculator(500, self.control_salary, self.control_spy,
                                                              self.control_goal)
        self.assertEqual(str(context.exception), "Age must be no less than 0 and no greater than 99 years.")

    def test_retirement_salary(self):
        """Tests initializing the RetirementCalculator object at varying salaries"""
        # Case: Salary is -500
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.retirement_calculator = RetirementCalculator(self.control_age, -500, self.control_spy,
                                                              self.control_goal)
        self.assertEqual(str(context.exception), "Salary must be no less than 0 and no greater than 500,000 USD.")

        # Case: Salary is 0
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.retirement_calculator = RetirementCalculator(self.control_age, 0, self.control_spy,
                                                              self.control_goal)
        self.assertEqual(str(context.exception), "Salary must be no less than 0 and no greater than 500,000 USD.")

        # Case: Salary is 1 (boundary)
        # expected: pass
        self.retirement_calculator = RetirementCalculator(self.control_age, 1, self.control_spy,
                                                          self.control_goal)

        # Case: Salary is 65000
        # expected: pass
        self.retirement_calculator = RetirementCalculator(self.control_age, 65000, self.control_spy,
                                                          self.control_goal)

        # Case: Salary is 500000 (boundary)
        # expected: pass
        self.retirement_calculator = RetirementCalculator(self.control_age, 500000, self.control_spy,
                                                          self.control_goal)

        # Case: Salary is 5000001
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.retirement_calculator = RetirementCalculator(self.control_age, 500001, self.control_spy,
                                                              self.control_goal)
        self.assertEqual(str(context.exception), "Salary must be no less than 0 and no greater than 500,000 USD.")

        # Case: Salary is 1000000
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.retirement_calculator = RetirementCalculator(self.control_age, 1000000, self.control_spy,
                                                              self.control_goal)
        self.assertEqual(str(context.exception), "Salary must be no less than 0 and no greater than 500,000 USD.")

    def test_retirement_spy(self):
        """Tests initializing the RetirementCalculator object at varying spys"""
        pass

    def test_retirement_goal(self):
        """Tests initializing the RetirementCalculator object at varying goals"""
        pass


if __name__ == '__main__':
    unittest.main()
