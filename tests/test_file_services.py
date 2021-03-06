from os import path

from services import file_services
from . import BaseTestCase


class TestFileServices(BaseTestCase):
    def test_should_write_data_to_file(self):

        file_services.write_lines_to_file(self.output_filename,
                                          self.expected_output_file_content)
        self.assertTrue(
            path.exists(self.output_filename),
            'Check if the function is creating the file if it not exists.')

        with open(self.output_filename, 'r') as test_file:
            file_content = test_file.readlines()

        self.assertEqual(
            len(file_content), 11,
            'Check if the function is writing all the lines to the file.')
        self.assertEqual(
            file_content, self.expected_output_file_content,
            'Check if the function is writing the data correctly to the file.')

    def test_should_return_default_tuple_if_file_does_not_exists(self):
        invalid_file = 'invalid.txt'
        error_message = """Check if the function is returning a tuple
        with the default values "(0, 0, [])",
        if the file does not exists."""

        returned_data = file_services.get_ttask_umax_and_new_users_from_file(
            invalid_file)
        expected_data = (0, 0, [])

        self.assertEqual(len(returned_data), 3, error_message)
        self.assertEqual(returned_data, expected_data, error_message)

    def test_should_return_ttask_umax_and_newuser_list_by_tick_from_file(self):

        returned_data = file_services.get_ttask_umax_and_new_users_from_file(
            self.input_filename)

        expected_data = (
            4,
            2,
            [1, 3, 0, 1, 0, 1],
        )
        self.assertEqual(len(returned_data), 3)
        self.assertEqual(returned_data, expected_data)

    def test_should_return_1_with_invalid_input(self):
        invalid_input_01 = '100'
        returned_value_01 = file_services.validate_ttask_umax_value(
            invalid_input_01)

        self.assertEqual(returned_value_01, 1)

        invalid_input_02 = '-50'
        returned_value_02 = file_services.validate_ttask_umax_value(
            invalid_input_02)

        self.assertEqual(returned_value_02, 1)

    def test_should_return_validated_value(self):
        valid_input_01 = ' 5   '
        returned_value_01 = file_services.validate_ttask_umax_value(
            valid_input_01)

        self.assertEqual(returned_value_01, 5)

        valid_input_02 = '\n \r 2  \n '
        returned_value_02 = file_services.validate_ttask_umax_value(
            valid_input_02)

        self.assertEqual(returned_value_02, 2)
