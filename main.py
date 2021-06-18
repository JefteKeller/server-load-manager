from services import file_services, server_services


def main(input_filename='input.txt', output_filename='output.txt') -> None:

    ttask_value, \
    umax_value, \
    new_users_by_cicle = file_services.get_ttask_umax_and_new_users_from_file(
        input_filename)

    server_cost_by_cicle = 1
    total_server_cost = 0

    output_log_lines = []
    server_list = []

    cicle_count = 0
    has_active_users = True

    while has_active_users:

        server_services.clean_completed_tasks(server_list, cicle_count)

        if cicle_count < len(new_users_by_cicle):
            new_users = new_users_by_cicle[cicle_count]

            if new_users:
                server_services.optimize_server_usage(server_list, umax_value)

            for _ in range(new_users):
                new_user = {'complete_at': cicle_count + ttask_value}

                available_server = server_services.get_available_server(
                    server_list, umax_value)
                server_services.register_user(new_user, available_server,
                                              server_list)

        server_services.shutdown_inactive_servers(server_list)

        new_log_line = server_services.generate_server_load_log(server_list)
        output_log_lines.append(new_log_line)

        total_server_cost += server_services.calculate_server_bill(
            server_list, server_cost_by_cicle)

        cicle_count += 1

        if not server_list:
            has_active_users = False

    output_log_lines.append(str(total_server_cost))
    file_services.write_lines_to_file(output_filename, output_log_lines)


if __name__ == '__main__':
    main()
