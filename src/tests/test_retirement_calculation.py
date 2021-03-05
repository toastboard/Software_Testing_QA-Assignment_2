# CJ Nguyen
# 2/23/2021

# Tests the calculations done in a RetirementCalculator object.

import unittest

from src.classes.retirement import RetirementCalculator


class TestRetirementCalculation(unittest.TestCase):
    def setUp(self):
        """Setup function that will apply to all other functions in the class.
        The items entered here must always result in a reachable goal.
        """
        # Age that must be valid
        self.control_age = 30
        # Salary that must be valid
        self.control_salary = 80000
        # Salary percentage saved per year that must be valid
        self.control_percent_savings = .12
        # Goal that must be valid
        self.control_goal = 700000

    def test_retirement_age(self):
        """Tests calculations at varying ages"""
        # Case: Age = 55
        # expected: savings age 55, goal not reachable
        self.retirement_calculator = RetirementCalculator(55, self.control_salary, self.control_percent_savings,
                                                          self.control_goal)
        self.assertEqual(55, self.retirement_calculator.calculate_savings_age())
        self.assertFalse(self.retirement_calculator.is_goal_reachable())

        # Case: Age = 45 (edge)
        # expected: savings age 55, goal not reachable
        self.retirement_calculator = RetirementCalculator(45, self.control_salary,
                                                          self.control_percent_savings, self.control_goal)
        self.assertEqual(55, self.retirement_calculator.calculate_savings_age())
        self.assertFalse(self.retirement_calculator.is_goal_reachable())

        # Case: Age = 25
        # expected: savings age 55, goal is reachable
        self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary,
                                                          self.control_percent_savings, self.control_goal)
        self.assertEqual(55, self.retirement_calculator.calculate_savings_age())
        self.assertTrue(self.retirement_calculator.is_goal_reachable())

    def test_retirement_salary(self):
        """Tests calculations at varying salaries"""
        # Case: Salary = 55,000
        # expected: savings age 79, goal not reachable
        self.retirement_calculator = RetirementCalculator(self.control_age, 55000,
                                                          self.control_percent_savings, self.control_goal)
        self.assertEqual(79, self.retirement_calculator.calculate_savings_age())
        self.assertFalse(self.retirement_calculator.is_goal_reachable())

        # Case:Salary = 61,729 (edge)
        # expected: savings age 70, goal not reachable
        self.retirement_calculator = RetirementCalculator(self.control_age, 61729,
                                                          self.control_percent_savings, self.control_goal)
        self.assertEqual(70, self.retirement_calculator.calculate_savings_age())
        self.assertFalse(self.retirement_calculator.is_goal_reachable())

        # Case: Age = 100,000 (control)
        # expected: savings age 55, goal is reachable
        self.retirement_calculator = RetirementCalculator(self.control_age, 100000,
                                                          self.control_percent_savings, self.control_goal)
        self.assertEqual(44, self.retirement_calculator.calculate_savings_age())
        self.assertTrue(self.retirement_calculator.is_goal_reachable())

    def test_retirement_percent_savings(self):
        """Tests calculations at varying percent saved per year"""
        # Case: Percent Savings = 0.08
        # expected: savings age 82, goal is reachable
        self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary,
                                                          0.08, self.control_goal)
        self.assertEqual(82, self.retirement_calculator.calculate_savings_age())
        self.assertFalse(self.retirement_calculator.is_goal_reachable())

        # Case: 0.093 (edge)
        # expected: savings age 70, goal not reachable
        self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary,
                                                          0.093, self.control_goal)
        self.assertEqual(70, self.retirement_calculator.calculate_savings_age())
        self.assertFalse(self.retirement_calculator.is_goal_reachable())

        # Case: Percent Savings = 0.15
        # expected: savings age 44, goal is reachable
        self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary,
                                                          0.15, self.control_goal)
        self.assertEqual(44, self.retirement_calculator.calculate_savings_age())
        self.assertTrue(self.retirement_calculator.is_goal_reachable())

    def test_retirement_goal(self):
        """Tests calculations at varying goals"""
        # Case: Goal = 1,000,000
        # expected: savings age 78, goal not reachable
        self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary,
                                                          self.control_percent_savings, 1000000)
        self.assertEqual(78, self.retirement_calculator.calculate_savings_age())
        self.assertFalse(self.retirement_calculator.is_goal_reachable())

        # Case: 907,200 (edge)
        # expected: savings age 70, goal not reachable
        self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary,
                                                          self.control_percent_savings, 907200)
        self.assertEqual(70, self.retirement_calculator.calculate_savings_age())
        self.assertFalse(self.retirement_calculator.is_goal_reachable())

        # Case: 500,000
        # expected: savings age 39, goal is reachable
        self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary,
                                                          self.control_percent_savings, 500000)
        self.assertEqual(39, self.retirement_calculator.calculate_savings_age())
        self.assertTrue(self.retirement_calculator.is_goal_reachable())

    def test_retirement_control(self):
        """Calculation with setUp variables"""
        # Case: Control
        # expected: savings age 55, goal is reachable
        self.retirement_calculator = RetirementCalculator(self.control_age, self.control_salary,
                                                          self.control_percent_savings, self.control_goal)
        self.assertEqual(55, self.retirement_calculator.calculate_savings_age())
        self.assertTrue(self.retirement_calculator.is_goal_reachable())


if __name__ == '__main__':
    unittest.main()
