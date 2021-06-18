from os import path

from main import main
from . import BaseTestCase


class TestMainApp(BaseTestCase):
    def test_should_not_manage_and_log_servers_with_invalid_file_content(self):
        output_filename = 'output.txt'
        expected_file_data = [
            '0\n',
            '0',
        ]
        invalid_filename = 'invalid.txt'
        main(invalid_filename)

        self.assertTrue(path.exists(output_filename))

        with open(output_filename, 'r') as output_file:
            output_file_data = output_file.readlines()

        self.assertEqual(len(output_file_data), 2)
        self.assertEqual(output_file_data, expected_file_data)

    def test_should_manage_and_log_servers(self):
        output_filename = 'output.txt'

        main(self.input_filename)

        self.assertTrue(path.exists(output_filename))

        with open(output_filename, 'r') as output_file:
            output_file_data = output_file.readlines()

        self.assertEqual(len(output_file_data),
                         len(self.expected_output_file_content))
        self.assertEqual(output_file_data, self.expected_output_file_content)
