# CJ Nguyen
# 2/23/2021

# Class containing the data and functionality for computing if a person's saving goal is realistically realizable

class RetirementCalculator:
    """Class of which each instance is capable of solving if a single person's ability to reach their savings goal
    before turning 100

    Attributes
    ----------
    age: the age of the person in years
    salary: the salary of the person in USD
    spy: stands for savings per year; percentage representing the portion of salary allocated to savings each year
    goal: the goal of the person the calculator will calculate for

    Methods
    -------
    """

    def __init__(self, age, salary, spy, goal):
        """Creates an instance of a RetirementCalculator object

        :param age: age in years
        :param salary: salary in USD
        :param spy: savings percentage per year
        :param goal: goal for savings in USD
        """
        self.age = age
        self.salary = salary
        self.goal = goal
        self.spy = spy

    def calculate_savings_age(self):
        pass

    def is_goal_reachable(self):
        pass