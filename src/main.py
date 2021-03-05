# CJ Nguyen
# 2/23/2021
# from .classes.bodymassindex import BodyMassIndex
# from .classes.retirement import RetirementCalculator
import os
import argparse


def retirement_calculator():
    while True:
        try:
            user_age = input("Enter age: ")
            user_salary = input("Enter salary: ")
            user_ = input("Enter percent of salary saved:")
            user_ = input("Enter savings goal:")
        except ValueError:
            print("ERROR:" + ValueError)
        except TypeError:
            print("ERROR:" + ValueError)
        print("1) Print inputted retirement values\n")
        print("2) Get amount of years before goal is met\n")
        print("3) Is retirement savings goal reachable before user is 100 years old?\n")
        print("4) Re-enter values\n")
        print("5) Step back to main menu\n")
        print("6) Exit program\n")

        while True:
            try:
                choice = int(input("Enter choice here (1-6): "))
                break
            except:

        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            return 1
        else:
            print("ERROR: Invalid entry, choose a number from 1-6.")





def bmi():
    pass


def tests():
    pass


def main():
    user_choice = input("Choose retirement calculator or BMI calculator and category checker? (retirement/bmi)\n"
                        "To exit, enter \"exit\".\n"
                        "Input: ")
    selection_made = 0
    while selection_made:
        if user_choice == "retirement":
            selection_made = retirement_calculator()
        elif user_choice == "bmi":
            selection_made = bmi()
        elif user_choice == "exit":
            return 1
        else:
            print("\nERROR: Incorrect choice made. Please enter one of three options - retiremet, bmi, or exit.\n\n")
    return 1


if __name__ == '__main__':
    main()
