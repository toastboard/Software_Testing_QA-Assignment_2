# CJ Nguyen
# 2/23/2021

# Class containing the data and functionality for computing body mass index
# (BMI) values and categories. Calculation for BMI sourced from
# http://extoxnet.orst.edu/faqs/dietcancer/web2/twohowto.html
from .bmi_categories import BodyMassIndexCategory


class BodyMassIndex:
    """Class of which each instance represents BMI measurements for a single
    person and offers functionality for calculating BMI values and
    discerning BMI categories.

    Attributes ---------- weight: weight of the person height: height of the
    person bmi_value: the body mass index value of a person rounded to the
    tenths place. bmi_category: the body mass category of a person

    Methods ------- calculate_body_mass_index: calculates the body mass
    index value using weight and height and sets the bmi_value and
    bmi_category attributes. get_weight: returns the weight attribute of the
    BodyMassIndex object get_height: returns the height attribute of the
    BodyMassIndex object get_bmi_value: returns the bmi_value attribute of
    the BodyMassIndex object get_bmi_category: returns the bmi_category
    attribute of the BodyMassIndex object

    NOTE: Because of the nature of Python floats, rounding the tenths place
    for the bmi_value attribute will sometimes result in unexpected output.
    For example, round(52.15) will give 52.1 despite round(52.16) giving 52.2.
    """

    def __init__(self, weight=None, height=None):
        """Creates an instance of a BodyMassIndex object.
        :param height: height in inches
        :type height: float
        :param weight: weight in pounds
        :type weight: float
        """
        if weight is not None and height is not None:
            try:
                weight = float(weight)
                height = float(height)
            except ValueError:
                raise (TypeError(
                    "Weight and height must be floating point integers."))
            if weight <= 0 or weight > 900:
                raise (ValueError(
                    "Weight must be greater than 0 and less than or equal to "
                    "900 pounds."))
            if height <= 0 or height > 108:
                # 108 is 9' in inches
                raise (ValueError(
                    "Height must be greater than 0 and less than or equal to "
                    "108 inches."))

            self.weight = weight
            self.height = height
            self.bmi_value = 0.0
            self.bmi_category = 0.0
            self.calculate_body_mass_index()

    def calculate_body_mass_index(self):
        """Calculates the BMI value given the weight and height attributes
        and sets the bmi_value and bmi_category accordingly
        """
        self.bmi_value = round(self.weight * 0.45 / pow(self.height * .025, 2),
                               1)

        if self.bmi_value < 18.5:
            self.bmi_category = BodyMassIndexCategory.UNDERWEIGHT
        elif self.bmi_value < 25.0:
            self.bmi_category = BodyMassIndexCategory.NORMAL_WEIGHT
        elif self.bmi_value < 30.0:
            self.bmi_category = BodyMassIndexCategory.OVER_WEIGHT
        else:
            self.bmi_category = BodyMassIndexCategory.OBESE

    def get_weight(self):
        """Returns the weight attribute"""
        return self.weight

    def get_height(self):
        """Returns the height attribute"""
        return self.height

    def get_bmi_value(self):
        """Returns the bmi_value attribute"""
        return self.bmi_value

    def get_bmi_category(self):
        """Returns the bmi_category attribute"""
        return self.bmi_category

    def __eq__(self, other):
        """Equivalency check override"""
        if type(self) != type(other):
            return False
        else:
            if not (not (self.weight != other.weight) and not (
                    self.height != other.height) and not (
                    self.bmi_value != other.bmi_value) and not (
                    self.bmi_category != other.bmi_category)):
                return False
            return True
