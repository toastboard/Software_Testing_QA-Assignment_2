# CJ Nguyen
# 2/23/2021

# Tests the BMI functionality of the program using the accessors and
# modifiers of the BodyMassIndex Python class.
import unittest

from src.classes.bmi_categories import BodyMassIndexCategory
from src.classes.bodymassindex import BodyMassIndex


class TestBMIInit(unittest.TestCase):
    def setUp(self):
        """Setup function that will apply to all other test functions in the
        class. """
        # Weight that must be valid
        self.control_bmi_weight = 125.0
        # Height that must be valid
        self.control_bmi_height = 63.0
        # The known value for the bmi value given the above weight and height
        self.control_bmi_value = 22.7
        # The known value for the bmi category given the above weight and
        # height
        self.control_bmi_category = BodyMassIndexCategory.NORMAL_WEIGHT

        # BodyMassIndex object that must be valid
        self.control_bmi_object = BodyMassIndex()
        self.control_bmi_object.weight = self.control_bmi_weight
        self.control_bmi_object.height = self.control_bmi_height
        self.control_bmi_object.calculate_body_mass_index()

    def test_bmi_weight_init(self):
        """Tests initializing a BodyMassIndex object with varying weights."""

        # Case: Weight of 0
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.bmi_object = BodyMassIndex(0.0, self.control_bmi_height)
        self.assertEqual(str(context.exception),
                         "Weight must be greater than 0 and less than or "
                         "equal to 900 pounds.")

        # Case: Weight of 900 (boundary)
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.bmi_object = BodyMassIndex(901.0, self.control_bmi_height)
        self.assertEqual(str(context.exception),
                         "Weight must be greater than 0 and less than or "
                         "equal to 900 pounds.")

        # Case: Weight of 1000
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.bmi_object = BodyMassIndex(1000.0, self.control_bmi_height)
        self.assertEqual(str(context.exception),
                         "Weight must be greater than 0 and less than or "
                         "equal to 900 pounds.")

        # Case: Weight of invalid type (str)
        # expected: TypeError
        with self.assertRaises(TypeError) as context:
            self.bmi_object = BodyMassIndex("test", self.control_bmi_height)
        self.assertEqual(str(context.exception),
                         "Weight and height must be floating point integers.")

        # Case: Valid Weight
        # expected: Pass
        self.bmi_object = BodyMassIndex(self.control_bmi_weight,
                                        self.control_bmi_height)

    def test_bmi_init_height(self):
        """Tests initializing a BodyMassIndex object with varying heights."""
        # Case: Height of 0
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.bmi_object = BodyMassIndex(self.control_bmi_weight, 0.0)
        self.assertEqual(str(context.exception),
                         "Height must be greater than 0 and less than or "
                         "equal to 108 inches.")

        # Case: Height of 108 (boundary)
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.bmi_object = BodyMassIndex(self.control_bmi_weight, 109.0)
        self.assertEqual(str(context.exception),
                         "Height must be greater than 0 and less than or "
                         "equal to 108 inches.")

        # Case: Height of 200
        # expected: ValueError
        with self.assertRaises(ValueError) as context:
            self.bmi_object = BodyMassIndex(self.control_bmi_weight, 0.0)
        self.assertEqual(str(context.exception),
                         "Height must be greater than 0 and less than or "
                         "equal to 108 inches.")

        # Case: Height of invalid type (str)
        # expected: TypeError
        with self.assertRaises(TypeError) as context:
            self.bmi_object = BodyMassIndex(self.control_bmi_weight, "test")
        self.assertEqual(str(context.exception),
                         "Weight and height must be floating point integers.")

        # Case: Valid Weight
        # expected: Pass
        self.bmi_object = BodyMassIndex(self.control_bmi_weight,
                                        self.control_bmi_height)

    def test_bmi_init_validity(self):
        """Tests to ensure that a BodyMassIndex object initiated with
        control variables passed as arguments match up with control
        BodyMassIndex object.
        """
        # Case: Initialize object, compare to control case.
        # expected: pass
        self.bmi_object = BodyMassIndex(self.control_bmi_weight,
                                        self.control_bmi_height)

        self.assertEqual(self.bmi_object, self.control_bmi_object)

    def test_bmi_accessors(self):
        """Tests the accessors provided by the BodyMassIndex class."""
        self.assertEqual(self.control_bmi_height,
                         self.control_bmi_object.get_height())
        self.assertEqual(self.control_bmi_weight,
                         self.control_bmi_object.get_weight())
        self.assertAlmostEqual(self.control_bmi_value,
                               self.control_bmi_object.get_bmi_value())
        self.assertEqual(self.control_bmi_category,
                         self.control_bmi_object.get_bmi_category())


if __name__ == '__main__':
    unittest.main()
