# CJ Nguyen
# 2/23/2021

# Enumerated list of different BMI categories.
# Source for BMI categories: https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html
from enum import Enum, auto


class BodyMassIndexCategory(Enum):
    """Enumerated class for finding BodyMassIndex categories"""
    # BMI value < 18.5
    UNDERWEIGHT = auto()
    # 18.5 <= BMI value < 25.0
    NORMAL_WEIGHT = auto()
    # 25.0 <= BMI value < 30
    OVER_WEIGHT = auto()
    # 30 <= BMI value
    OBESE = auto()
