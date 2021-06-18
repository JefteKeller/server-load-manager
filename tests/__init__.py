from os import path, remove
from unittest import TestCase


class BaseTestCase(TestCase):
    def setUp(self):
        self.input_filename = 'test_input.txt'
        self.output_filename = 'test_output.txt'

        input_file_data = [
            '4\n',
            '2\n',
            '1\n',
            '3\n',
            '0\n',
            '1\n',
            '0\n',
            '1\n',
        ]
        with open(self.input_filename, 'w') as test_input_file:
            test_input_file.writelines(input_file_data)

        self.expected_output_file_content = [
            '1\n',
            '2,2\n',
            '2,2\n',
            '2,2,1\n',
            '1,2,1\n',
            '2\n',
            '2\n',
            '1\n',
            '1\n',
            '0\n',
            '15',
        ]

    def tearDown(self):
        if path.exists(self.input_filename):
            remove(self.input_filename)

        if path.exists(self.output_filename):
            remove(self.output_filename)
