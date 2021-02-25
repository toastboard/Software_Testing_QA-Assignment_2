# CJ Nguyen
# 2/23/2021

# Class containing the data and functionality for computing body mass index (BMI) values and categories.
# Calculation for BMI sourced from http://extoxnet.orst.edu/faqs/dietcancer/web2/twohowto.html


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
    calculate_body_mass_index: calculates the body mass index value using weight and height and sets the bmi_value and
    bmi_category attributes.
    get_weight: returns the weight attribute of the BodyMassIndex object
    get_height: returns the height attribute of the BodyMassIndex object
    get_bmi_value: returns the bmi_value attribute of the BodyMassIndex object
    get_bmi_category: returns the bmi_category attribute of the BodyMassIndex object
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
            self.bmi_value = None
            self.bmi_category = None
            self.calculate_body_mass_index()

    def calculate_body_mass_index(self):
        """Calculates the BMI value given the weight and height attributes and sets the bmi_value and bmi_category
        accordingly
        """
        pass

    def get_weight(self):
        """Returns the weight attribute"""
        pass

    def get_height(self):
        """Returns the height attribute"""
        pass

    def get_bmi_value(self):
        """Returns the bmi_value attribute"""
        pass

    def get_bmi_category(self):
        """Returns the bmi_category attribute"""
        pass

    def __eq__(self, other):
        """Equivalency check override"""
        if type(self) != type(other):
            return False
        else:
            if not (not (self.weight != other.weight) and not (self.height != other.height) and not (
                    self.bmi_value != other.bmi_value) and not (self.bmi_category != other.bmi_category)):
                return False
            return True
