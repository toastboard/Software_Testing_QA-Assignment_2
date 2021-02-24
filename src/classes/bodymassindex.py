# CJ Nguyen
# 2/23/2021

class BodyMassIndex:
    """Class of which each instance represents BMI measurements for a single person and offers functionality for
    calculating BMI values and discerning BMI categories.

    Attributes
    ----------
    weight: weight of the person
    height: height of the person
    bmi_value: the body mass index value of a person
    bmi_category: the body mass category of a person

    Methods
    -------
    calculate_body_mass_index: calculates the body mass index value using weight and height and returns it.
    get_bmi_category: discerns the bmi category from the body mass index
    """

    def __init__(self, weight=None, height=None):
        """Creates an instance of a BodyMassIndex object.
        :param height: height in inches
        :type height: float
        :param weight: weight in pounds
        :type weight: float
        """
        if weight is not None and height is not None:
            if type(weight) != float or type(height) != float:
                raise (TypeError("Weight and height must be floating point integers."))
            if weight <= 0 or weight > 900:
                raise (ValueError("Weight must be greater than 0 and less than or equal to 900 pounds."))
            if height <= 0 or height > 108:
                # 108 is 9' in inches
                raise (ValueError("Height must be greater than 0 and less than or equal to 108 inches."))

            self.weight = weight
            self.height = height

            self.bmi_value = self.calculate_body_mass_index

    def calculate_body_mass_index(self):
        pass

    def get_bmi_category(self):
        pass

    def get_weight(self):
        pass

    def get_height(self):
        pass

    def get_bmi_value(self):
        pass

    def __eq__(self, other):
        """Equivalency check override"""
        if type(self) != type(other):
            return False
        else:
            if self.weight != other.weight or self.height != other.height:
                return False
            return True
