# CJ Nguyen
# 2/23/2021
#  from .classes.bodymassindex import BodyMassIndex
from src.classes.retirement import RetirementCalculator


def retirement_calculator():
    while True:
        retirement_calc = None
        try:
            print("Enter all values as whole numbers with no commas except percent savings. Percent savings must be a "
                  "decimal less than one and greater than zero.")
            user_age = input("Enter age: ")
            user_salary = input("Enter salary: ")
            user_percent_savings = input("Enter percent of salary saved: ")
            user_goal = input("Enter savings goal: ")

            retirement_calc = RetirementCalculator(user_age, user_salary, user_percent_savings, user_goal)
        except ValueError as e:
            print("ERROR:" + str(e))
            print("")
            continue
        except TypeError as e:
            print("ERROR:" + str(e))
            print("")
            continue
        except:
            exit(1)

        print("1) Print inputted retirement values")
        print("2) Get amount of years before goal is met")
        print("3) Is retirement savings goal reachable before user is 100 years old?")
        print("4) Re-enter values")
        print("5) Step back to main menu")
        print("6) Exit program\n")

        test = 1
        while test == 1:
            choice = 0
            try:
                choice = int(input("Enter choice here (1-6): "))
            except ValueError as e:
                if "invalid literal for int()" in str(e):
                    print("\nERROR: Integer required.\n")
                continue

            if choice == 1:
                print("Age:" + str(retirement_calc.get_age()))
                print("Salary: " + str(retirement_calc.get_salary()))
                print("Percent Savings: " + str(retirement_calc.get_percent_savings()))
                print("Goal: " + str(retirement_calc.get_goal()))
                print("")
            elif choice == 2:
                print("Years to goal: " + str(retirement_calc.calculate_savings_age()))
                print("")
            elif choice == 3:
                if retirement_calc.is_goal_reachable():
                    print("Goal is reachable before user turns 100 years old.")
                else:
                    print("Goal is not reachable before user turns 100 years old.")
                print("")
            elif choice == 4:
                test = 0
            elif choice == 5:
                return 0
            elif choice == 6:
                return 1
            else:
                print("\nERROR: Invalid entry, choose a number from 1-6.\n")


def bmi():
    


def tests():
    pass


def main():
    selection_made = 0
    while selection_made == 0:
        user_choice = input("Choose retirement calculator or BMI calculator and category checker? (retirement/bmi)\n"
                            "To exit, enter \"exit\".\n"
                            "Input: ")
        if user_choice.lower() == "retirement":
            selection_made = retirement_calculator()
        elif user_choice.lower() == "bmi":
            selection_made = bmi()
        elif user_choice == "exit":
            return 1
        else:
            print("\nERROR: Invalid choice made. Please enter one of three options - retiremet, bmi, or exit.\n\n")
    return 1


if __name__ == '__main__':
    main()
