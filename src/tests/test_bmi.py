# CJ Nguyen
# 2/23/2021

# Tests the BMI functionality of the program using the accessors and modifiers of the BodyMassIndex Python class.
import unittest
from ..classes.bodymassindex import BodyMassIndex


class TestBMI(unittest.TestCase):
    def setUp(self):
        """Setup function that will apply to all other test functions in the class."""
        self.control_bmi_object = BodyMassIndex()
        self.control_bmi_object.height = 63.0
        self.control_bmi_object.weight = 125.0

    def test_bmi_init(self):
        """Tests initializing a BodyMassIndex class object"""
        with self.assertRaises(ValueError) as context:
            self.bmi_object = BodyMassIndex(0, 125)

        self.bmi_object = BodyMassIndex(63, 125)


    def test_bmi_value_calculation(self):
        """Tests the calculation of a bmi value with the BodyMassIndex class object"""
        pass

    def test_bmi_category_calculation(self):
        """Tests initializing a BodyMassIndex class object"""
        pass
