import unittest
from ..classes.bmi_categories import BodyMassIndexCategory
from ..classes.bodymassindex import BodyMassIndex


class TestBMICalculations(unittest.TestCase):
    def setUp(self):
        """Setup function that will apply to all other test functions in the class.
        All BMI values are calculated using a calculator with the calculation given in
        http://extoxnet.orst.edu/faqs/dietcancer/web2/twohowto.html

        The height values will be kept consistently at 63.
        Each weight will change per case and the expected value and category for each case are set up beforehand.
        """
        # A height that will be used for all test cases in order to have a uniform test spread.
        self.control_height = 63

        # Values representing an obese BMI category.
        self.obese_weight = 190
        self.obese_value = 34.5
        self.obese_category = BodyMassIndexCategory.OBESE

        # Values representing the edge case between the overweight and obese categories.
        self.overweight_obese_weight = 165.375
        self.overweight_obese_value = 30
        self.overweight_obese_category = BodyMassIndexCategory.OBESE

        # Values representing an overweight BMI category
        self.overweight_weight = 150
        self.overweight_value = 27.2
        self.overweight_category = BodyMassIndexCategory.OVER_WEIGHT

        # Values representing the edge case between the normal and overweight categories.
        self.normal_overweight_weight = 137.81
        self.normal_overweight_value = 25
        self.normal_overweight_category = BodyMassIndexCategory.OVER_WEIGHT

        # Values representing a normal BMI category
        self.normal_weight = 120
        self.normal_value = 21.8
        self.normal_category = BodyMassIndexCategory.NORMAL_WEIGHT

        # Values representing the edge case between the underweight and normal categories.
        self.underweight_normal_weight = 101.98
        self.underweight_normal_value = 18.5
        self.underweight_normal_category = BodyMassIndexCategory.NORMAL_WEIGHT

        # Values representing an underweight BMI category
        self.underweight_weight = 90
        self.underweight_value = 16.3
        self.underweight_category = BodyMassIndexCategory.UNDERWEIGHT

    def test_bmi_obese(self):
        pass

    def test_bmi_overweight(self):
        pass

    def test_bmi_normal(self):
        pass

    def test_bmi_underweight(self):
        pass

if __name__ == '__main__':
    unittest.main()
