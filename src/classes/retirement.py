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
        if not 0 <= age < 100:
            raise ValueError("Age must be no less than 0 and no greater than 99 years.")
        if not 0 < salary <= 500000:
            raise ValueError("Salary must be greater than 0 and no greater than 500,000 USD.")
        if not 0 < spy < 1:
            raise ValueError("Savings per year must be greater than 0 and less than 1.")
        if not 0 < goal <= 2000000:
            raise ValueError("Savings goal must be greater than 0 and no greater than 2,000,000 USD.")
        self.age = age
        self.salary = salary
        self.spy = spy
        self.goal = goal

    def calculate_savings_age(self):
        pass

    def is_goal_reachable(self):
        pass