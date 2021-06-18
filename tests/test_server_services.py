from services import server_services

from . import BaseTestCase


class TestServerServices(BaseTestCase):
    def test_should_return_available_server(self):
        test_servers = []
        test_umax = 2

        returned_server = server_services.get_available_server(
            test_servers, test_umax)

        self.assertEqual(len(returned_server), 0)
        self.assertIsInstance(returned_server, list)

        test_servers = [
            [{
                'test_dict': 0
            }, {
                'test_dict': 1
            }],
            [{
                'test_dict_2': 2
            }],
        ]
        returned_server = server_services.get_available_server(
            test_servers, test_umax)

        self.assertEqual(len(returned_server), 1)
        self.assertEqual(returned_server, test_servers[1])
        self.assertDictEqual(test_servers[1][0], returned_server[0])

    def test_should_register_user(self):
        test_servers = []
        test_user_01 = {'complete_at': 1}

        server_services.register_user(test_user_01, [], test_servers)

        self.assertEqual(len(test_servers), 1)
        self.assertDictEqual(test_servers[0][0], test_user_01)

        test_user_02 = {'complete_at': 2}

        server_services.register_user(test_user_02, test_servers[0],
                                      test_servers)

        self.assertEqual(len(test_servers), 1)
        self.assertDictEqual(test_servers[0][1], test_user_02)

    def test_should_optimize_server_usage(self):
        test_servers = [[{'complete_at': 7}], [{'complete_at': 9}]]
        test_umax = 2

        expected_servers = [[{'complete_at': 7}, {'complete_at': 9}]]

        server_services.optimize_server_usage(test_servers, test_umax)

        self.assertEqual(len(test_servers), 1)
        self.assertEqual(test_servers, expected_servers)

        self.assertEqual(test_servers[0][0], expected_servers[0][0])
        self.assertEqual(test_servers[0][1], expected_servers[0][1])

    def test_should_clean_completed_tasks(self):
        test_servers = [[{'complete_at': 7}], [{'complete_at': 9}]]
        test_cicle = 8

        expected_servers = [[], [{'complete_at': 9}]]

        server_services.clean_completed_tasks(test_servers, test_cicle)

        self.assertEqual(len(test_servers), 2)
        self.assertEqual(expected_servers, test_servers)

        self.assertEqual(test_servers[0], expected_servers[0])
        self.assertEqual(test_servers[1][0], expected_servers[1][0])

    def test_should_shutdown_inactive_servers(self):
        test_servers = [[], [{'complete_at': 9}]]
        expected_servers = [[{'complete_at': 9}]]

        server_services.shutdown_inactive_servers(test_servers)

        self.assertEqual(len(test_servers), 1)
        self.assertEqual(test_servers, expected_servers)
        self.assertEqual(test_servers[0][0], expected_servers[0][0])

    def test_should_generate_server_load_log(self):
        test_servers = []
        expected_log_line_01 = '0\n'

        returned_log_line_01 = server_services.generate_server_load_log(
            test_servers)

        self.assertEqual(returned_log_line_01, expected_log_line_01)

        test_servers = [[{'complete_at': 7}], [{'complete_at': 9}]]
        expected_log_line_02 = '1,1\n'

        returned_log_line_02 = server_services.generate_server_load_log(
            test_servers)

        self.assertEqual(returned_log_line_02, expected_log_line_02)

    def test_should_calculate_server_bill(self):
        test_servers = []
        test_server_cost = 2

        returned_server_bill = server_services.calculate_server_bill(
            test_servers, test_server_cost)

        self.assertEqual(returned_server_bill, 0)

        test_servers = [[{'complete_at': 7}], [{'complete_at': 9}]]

        returned_server_bill = server_services.calculate_server_bill(
            test_servers, test_server_cost)

        self.assertEqual(returned_server_bill, 4)
