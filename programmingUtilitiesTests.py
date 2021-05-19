import unittest
import programmingUtilities


class TestComparisonToolsMethods(unittest.TestCase):

    def setUp(self):
        self.programing_utilities = programmingUtilities.ComparisonTools()
        self.example_list1 = ["Cat", "Dog", "Panda", "Rat", "Cat", "Human", "Panda", "Left", "Dog"]
        self.example_list2 = ["Car", "The", "Sky", "Panda", "No", "Ink", "Blue", "Yes", "Life", "Cat", "Bird"]

    def test_remove_duplicates_from_list(self):
        # arrange
        test_list = self.example_list1
        # self.example_list1 = ["Cat", "Dog", "Panda", "Rat", "Cat", "Human", "Panda", "Left", "Dog"]
        final_list = ["Cat", "Dog", "Human", "Left", "Panda", "Rat"]

        # act
        unique_values_from_list = self.programing_utilities.remove_duplicates_from_list(test_list)

        # assert
        self.assertEqual(unique_values_from_list, final_list)

programming_utilities_test_suite = unittest.TestLoader().loadTestsFromTestCase(TestComparisonToolsMethods)
unittest.TextTestRunner(verbosity=2).run(programming_utilities_test_suite)
