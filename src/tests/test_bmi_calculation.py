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
        self.control_height = 63.0

        # Values representing an obese BMI category.
        self.obese_weight = 190.0
        self.obese_value = 34.5
        self.obese_category = BodyMassIndexCategory.OBESE

        # Values representing the edge case between the overweight and obese categories.
        self.overweight_obese_weight = 165.375
        self.overweight_obese_value = 30
        self.overweight_obese_category = BodyMassIndexCategory.OBESE

        # Values representing an overweight BMI category
        self.overweight_weight = 150.0
        self.overweight_value = 27.2
        self.overweight_category = BodyMassIndexCategory.OVER_WEIGHT

        # Values representing the edge case between the normal and overweight categories.
        self.normal_overweight_weight = 137.81
        self.normal_overweight_value = 25
        self.normal_overweight_category = BodyMassIndexCategory.OVER_WEIGHT

        # Values representing a normal BMI category
        self.normal_weight = 120.0
        self.normal_value = 21.8
        self.normal_category = BodyMassIndexCategory.NORMAL_WEIGHT

        # Values representing the edge case between the underweight and normal categories.
        self.underweight_normal_weight = 101.98
        self.underweight_normal_value = 18.5
        self.underweight_normal_category = BodyMassIndexCategory.NORMAL_WEIGHT

        # Values representing an underweight BMI category
        self.underweight_weight = 90.0
        self.underweight_value = 16.3
        self.underweight_category = BodyMassIndexCategory.UNDERWEIGHT

    def test_bmi_obese(self):
        """Tests the obese values case"""
        self.bmi_object = BodyMassIndex(self.obese_weight, self.control_height)

        self.assertAlmostEqual(self.bmi_object.get_bmi_value(), self.obese_value)
        self.assertEqual(self.bmi_object.get_bmi_category(), self.obese_category)

    def test_bmi_overweight_obese_edge(self):
        """Tests the overweight-obese value edge case"""
        self.bmi_object = BodyMassIndex(self.overweight_obese_weight, self.control_height)

        self.assertAlmostEqual(self.bmi_object.get_bmi_value(), self.overweight_obese_value)
        self.assertEqual(self.bmi_object.get_bmi_category(), self.overweight_obese_category)

    def test_bmi_overweight(self):
        """Tests the overweight values case"""
        self.bmi_object = BodyMassIndex(self.overweight_weight, self.control_height)

        self.assertAlmostEqual(self.bmi_object.get_bmi_value(), self.overweight_value)
        self.assertEqual(self.bmi_object.get_bmi_category(), self.overweight_category)

    def test_bmi_normal_overweight_edge(self):
        """Tests the normal-overweight value edge case"""
        self.bmi_object = BodyMassIndex(self.normal_overweight_weight, self.control_height)

        self.assertAlmostEqual(self.bmi_object.get_bmi_value(), self.normal_overweight_value)
        self.assertEqual(self.bmi_object.get_bmi_category(), self.normal_overweight_category)
        
    def test_bmi_normal(self):
        """Tests the normal values case"""
        self.bmi_object = BodyMassIndex(self.normal_weight, self.control_height)

        self.assertAlmostEqual(self.bmi_object.get_bmi_value(), self.normal_value)
        self.assertEqual(self.bmi_object.get_bmi_category(), self.normal_category)
        
    def test_bmi_underweight_normal_edge(self):
        """Tests the underweight-normal value edge case"""
        self.bmi_object = BodyMassIndex(self.underweight_normal_weight, self.control_height)

        self.assertAlmostEqual(self.bmi_object.get_bmi_value(), self.underweight_normal_value)
        self.assertEqual(self.bmi_object.get_bmi_category(), self.underweight_normal_category)
        
    def test_bmi_underweight(self):
        """Tests the underweight values case"""
        self.bmi_object = BodyMassIndex(self.underweight_weight, self.control_height)

        self.assertAlmostEqual(self.bmi_object.get_bmi_value(), self.underweight_value)
        self.assertEqual(self.bmi_object.get_bmi_category(), self.underweight_category)


if __name__ == '__main__':
    unittest.main()
