# CJ Nguyen
# 2/23/2021

# Class containing the data and functionality for computing if a person's
# saving goal is realistically realizable
from math import ceil


class RetirementCalculator:
    """Class of which each instance is capable of solving if a single
    person's ability to reach their savings goal before turning 100

    Attributes ---------- age: the age of the person in years salary: the
    salary of the person in USD percent_savings: stands for savings per
    year; percentage representing the portion of salary allocated to savings
    each year goal: the goal of the person the calculator will calculate for

    Methods ------- calculate_savings_age: calculates the age at which the
    person will achieve their savings goal given the values in the
    attributes is_goal_reachable: tells if goal is reachable (goal can be
    reached before person turns 100)
    """

    def __init__(self, age, salary, percent_savings, goal):
        """Creates an instance of a RetirementCalculator object.

        :param age: age in years
        :param salary: salary in USD
        :param percent_savings: savings percentage per year
        :param goal: goal for savings in USD
        """
        try:
            age = int(age)
            salary = int(salary)
            percent_savings = float(percent_savings)
            goal = int(goal)
        except ValueError:
            raise TypeError("Input was of incorrect type")
        if not 0 <= age < 100:
            raise ValueError(
                "Age must be no less than 0 and no greater than 99 years.")
        if not 0 < salary <= 500000:
            raise ValueError(
                "Salary must be greater than 0 and no greater than 500,"
                "000 USD.")
        if not 0.0 < percent_savings < 1.0:
            raise ValueError(
                "Savings per year must be greater than 0 and less than 1.")
        if not 0 < goal <= 2000000:
            raise ValueError(
                "Savings goal must be greater than 0 and no greater than 2,"
                "000,000 USD.")
        self.age = age
        self.salary = salary
        self.percent_savings = percent_savings
        self.goal = goal

    def calculate_savings_age(self):
        """Returns the number of years until the person's saving goals will be
        met.

        :return: the number of years until the goal is met
        """
        savings_per_year = self.salary * self.percent_savings * 1.35
        years_to_goal = ceil(self.goal / savings_per_year)
        return years_to_goal

    def is_goal_reachable(self):
        """Returns if the savings goal is reachable.

        :return: True if age + years to goal is less than 100, else false.
        """
        if self.age + self.calculate_savings_age() >= 100:
            return False
        else:
            return True

    def get_age(self):
        """Returns age attribute"""
        return self.age

    def get_salary(self):
        """Returns age attribute"""
        return self.salary

    def get_percent_savings(self):
        """Returns percent saved per year attribute"""
        return self.percent_savings

    def get_goal(self):
        """Returns goal attribute"""
        return self.goal
