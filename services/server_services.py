def get_available_server(server_list: list[list], umax: int) -> list:
    """Search for a server that has the capacity to hold a user.

    Args:
        server_list (list): a list of servers.
        umax (int): capacity of each server.

    Returns:
        list: an available server or a empty list in case there is none.
    """
    for server in server_list:
        if len(server) < umax:
            return server

    return []


def register_user(user: dict, server: list, server_list: list[list]):
    """Add a new user to a server.

    In case the server is not available,
    create a new server with the user, and register it into the server list.

    Args:
        new_user (dict): user to register.
        server (list): a server to register the user in case it is available.
        server_list (list): a list of servers.
    """
    if server:
        server.append(user)
    else:
        new_server = [user]
        server_list.append(new_server)


def optimize_server_usage(server_list: list[list], umax: int) -> None:
    """Optimize the use of the servers, merging servers.

    Args:
        server_list (list): [description]
        umax (int): [description]
    """
    optimized_server_list = []

    for server in server_list:
        if len(server) == umax:
            optimized_server_list.append(server)
        else:
            for user in server:
                new_server = get_available_server(optimized_server_list, umax)
                register_user(user, new_server, optimized_server_list)

    server_list[:] = optimized_server_list


def clean_completed_tasks(server_list: list[list], current_cicle: int) -> None:
    """Remove completed tasks from the servers.

    Iterates over a list of servers,
    and keep only the tasks that completes their cicle after the current one.

    Args:
        server_list (list): a list of servers.
        current_cicle (int): number of the current iteration.
    """
    for server in server_list:
        server[:] = [
            user for user in server if user['complete_at'] > current_cicle
        ]


def shutdown_inactive_servers(server_list: list[list]) -> None:
    """Remove unused servers.

    Iterate over a list of servers and keep those with active tasks.

    Args:
        server_list (list): a list of servers.
    """
    server_list[:] = [server for server in server_list if server]


def generate_server_load_log(server_list: list[list]) -> str:
    """Create a string logging the Server Load.

    Args:
        server_list (list): a list of servers.

    Returns:
        str: a line with the server load separated by commas, ending in a newline.
    """
    new_log_line = '0\n'

    server_load = [str(len(server)) for server in server_list]

    if server_load:
        new_log_line = ','.join(server_load) + '\n'

    return new_log_line


def calculate_server_bill(server_list: list[list], server_cost: int) -> int:
    """Calculate the server costs for each cicle.

    Args:
        server_list (list): a list of servers.
        server_cost (int): server cost by cicle.

    Returns:
        int: server cost for the current cicle.
    """
    return len(server_list) * server_cost
