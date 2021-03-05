# CJ Nguyen
# 2/23/2021

# Tests the creation of RetirementCalculator Objects

import unittest

from src.classes.retirement import RetirementCalculator


class TestRetirementInit(unittest.TestCase):
    def setUp(self):
        """Setup function that will apply to all other functions in the class."""
        # Age that must be valid
        self.control_age = 30
        # Salary that must be valid
        self.control_salary = 80000
        # Salary percentage saved per year that must be valid
        self.control_percent_savings = .12
        # Goal that must be valid
        self.control_goal = 700000

    def test_retirement_age_init(self):
        """Tests initializing the RetirementCalculator object at varying ages."""
        # Case: Age is -500
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.retirement_calculator = RetirementCalculator(-500, self.control_salary, self.control_percent_savings,
                                                              self.control_goal)
        self.assertEqual(str(context.exception), "Age must be no less than 0 and no greater than 99 years.")

        # Case: Age is -1
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.retirement_calculator = RetirementCalculator(-1, self.control_salary, self.control_percent_savings,
                                                              self.control_goal)
        self.assertEqual(str(context.exception), "Age must be no less than 0 and no greater than 99 years.")

        # Case: Age is 0 (boundary)
        # expected: pass
        self.retirement_calculator = RetirementCalculator(0, self.control_salary, self.control_percent_savings,
                                                          self.control_goal)

        # Case: Age is 30 (control)
        # expected: pass
        self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary,
                                                          self.control_percent_savings,
                                                          self.control_goal)

        # Case: Age is 99 (boundary)
        # expected: pass
        self.retirement_calculator = RetirementCalculator(99, self.control_salary, self.control_percent_savings,
                                                          self.control_goal)

        # Case: Age is 100
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.retirement_calculator = RetirementCalculator(100, self.control_salary, self.control_percent_savings,
                                                              self.control_goal)
        self.assertEqual(str(context.exception), "Age must be no less than 0 and no greater than 99 years.")

        # Case: Age is 500
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.retirement_calculator = RetirementCalculator(500, self.control_salary, self.control_percent_savings,
                                                              self.control_goal)
        self.assertEqual(str(context.exception), "Age must be no less than 0 and no greater than 99 years.")

    def test_retirement_salary(self):
        """Tests initializing the RetirementCalculator object at varying salaries"""
        # Case: Salary is -500
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.retirement_calculator = RetirementCalculator(self.control_age, -500, self.control_percent_savings,
                                                              self.control_goal)
        self.assertEqual(str(context.exception), "Salary must be greater than 0 and no greater than 500,000 USD.")

        # Case: Salary is 0
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.retirement_calculator = RetirementCalculator(self.control_age, 0, self.control_percent_savings,
                                                              self.control_goal)
        self.assertEqual(str(context.exception), "Salary must be greater than 0 and no greater than 500,000 USD.")

        # Case: Salary is 1 (boundary)
        # expected: pass
        self.retirement_calculator = RetirementCalculator(self.control_age, 1, self.control_percent_savings,
                                                          self.control_goal)

        # Case: Salary is 80000 (control)
        # expected: pass
        self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary,
                                                          self.control_percent_savings,
                                                          self.control_goal)

        # Case: Salary is 500000 (boundary)
        # expected: pass
        self.retirement_calculator = RetirementCalculator(self.control_age, 500000, self.control_percent_savings,
                                                          self.control_goal)

        # Case: Salary is 500001
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.retirement_calculator = RetirementCalculator(self.control_age, 500001, self.control_percent_savings,
                                                              self.control_goal)
        self.assertEqual(str(context.exception), "Salary must be greater than 0 and no greater than 500,000 USD.")

        # Case: Salary is 1000000
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.retirement_calculator = RetirementCalculator(self.control_age, 1000000, self.control_percent_savings,
                                                              self.control_goal)
        self.assertEqual(str(context.exception), "Salary must be greater than 0 and no greater than 500,000 USD.")

    def test_retirement_percent_savings(self):
        """Tests initializing the RetirementCalculator object at varying percent saved per year"""
        # Case: Savings per year is -10
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary, -10,
                                                              self.control_goal)
        self.assertEqual(str(context.exception), "Savings per year must be greater than 0 and less than 1.")

        # Case: Savings per year is 0
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary, 0,
                                                              self.control_goal)
        self.assertEqual(str(context.exception), "Savings per year must be greater than 0 and less than 1.")

        # Case: Savings per year is 0.01
        # expected: pass
        self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary, 0.01,
                                                          self.control_goal)

        # Case: Savings per year is 0.12 (control)
        # expected: pass
        self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary,
                                                          self.control_percent_savings,
                                                          self.control_goal)

        # Case: Savings per year is 0.99
        # expected: pass
        self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary, 0.99,
                                                          self.control_goal)

        # Case: Savings per year is 1
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary, 1,
                                                              self.control_goal)
        self.assertEqual(str(context.exception), "Savings per year must be greater than 0 and less than 1.")

        # Case: Savings per year is 10
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary, 10,
                                                              self.control_goal)
        self.assertEqual(str(context.exception), "Savings per year must be greater than 0 and less than 1.")

    def test_retirement_goal(self):
        """Tests initializing the RetirementCalculator object at varying goals"""
        # Case: Goal is -1000
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary,
                                                              self.control_percent_savings,
                                                              -1000)
        self.assertEqual(str(context.exception),
                         "Savings goal must be greater than 0 and no greater than 2,000,000 USD.")

        # Case: Goal is 0
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary,
                                                              self.control_percent_savings,
                                                              0)
        self.assertEqual(str(context.exception),
                         "Savings goal must be greater than 0 and no greater than 2,000,000 USD.")

        # Case: Goal is 1 (boundary)
        # expected: pass
        self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary,
                                                          self.control_percent_savings,
                                                          1)

        # Case: Goal is 700000 (control)
        # expected: pass
        self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary,
                                                          self.control_percent_savings,
                                                          self.control_goal)

        # Case: Goal is 2000000 (boundary)
        # expected: pass
        self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary,
                                                          self.control_percent_savings,
                                                          2000000)

        # Case: Goal is 2000001
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary,
                                                              self.control_percent_savings,
                                                              2000001)
        self.assertEqual(str(context.exception),
                         "Savings goal must be greater than 0 and no greater than 2,000,000 USD.")

        # Case: Goal is 10000000
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary,
                                                              self.control_percent_savings,
                                                              10000000)
        self.assertEqual(str(context.exception),
                         "Savings goal must be greater than 0 and no greater than 2,000,000 USD.")

    def test_diff_types(self):
        """Tests initializing the Retirement Calculator object with erroneous types passed in."""
        # Case: String for age
        # expected: TypeError
        with self.assertRaises(TypeError):
            self.retirement_calculator = RetirementCalculator("test", self.control_salary, self.control_percent_savings,
                                                              self.control_goal)
        # Case: String for salary
        # expected: TypeError
        with self.assertRaises(TypeError):
            self.retirement_calculator = RetirementCalculator(self.control_age, "test", self.control_percent_savings,
                                                              self.control_goal)
        # Case: String for savings per year
        # expected: TypeError
        with self.assertRaises(TypeError):
            self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary, "test",
                                                              self.control_goal)
        # Case: String for goal
        # expected: TypeError
        with self.assertRaises(TypeError):
            self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary,
                                                              self.control_percent_savings,
                                                              "test")

    def test_getters(self):
        """Tests the getters of the RetirementCalculator class"""
        self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary,
                                                          self.control_percent_savings, self.control_goal)

        # Case: Age
        # expected: 30
        self.assertEqual(self.control_age, self.retirement_calculator.get_age())

        # Case: Salary
        # expected: 80,000
        self.assertEqual(self.control_salary, self.retirement_calculator.get_salary())

        # Case: Percent Saved per Year
        # expected: 0.12
        self.assertEqual(self.control_percent_savings, self.retirement_calculator.get_percent_savings())

        # Case: Goal
        # expected: 700,000
        self.assertEqual(self.control_goal, self.retirement_calculator.get_goal())


if __name__ == '__main__':
    unittest.main()
