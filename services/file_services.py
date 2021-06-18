from os import path


def validate_ttask_umax_value(raw_value: str) -> int:
    """Remove the spaces, convert to integer and validate the value.

    Valid input: 1 <= value <= 10

    Args:
        raw_value (str): 'ttask' or 'umax' input from file.

    Returns:
        int: converted and validated value, according to the limits.
    """
    value = int(raw_value.strip())

    if 1 <= value <= 10:
        return value

    return 1


def get_ttask_umax_and_new_users_from_file(filename: str) -> tuple:
    """Read the file and return a tuple with: ttask,
    umax and a list with the number of new users on each tick.

    Args:
        filename (str): string indicating the path to the file.

    Returns:
        tuple with: ttask, umax and a list of how many new users by cicle.
    """

    if not path.exists(filename):
        return (0, 0, [])

    with open(filename, 'r') as input_file:

        # First line of file - Has the 'ttask' value
        ttask_value = validate_ttask_umax_value(input_file.readline())

        # Second line of file - Has the 'umax' value
        umax_value = validate_ttask_umax_value(input_file.readline())

        # The other lines contain the number of new users for each cicle
        new_users_by_tick = [int(user.strip()) for user in input_file]

    return (
        ttask_value,
        umax_value,
        new_users_by_tick,
    )


def write_lines_to_file(filename: str, file_data: list[str]) -> None:
    """Write a list of strings into the file.

    Args:
        filename (str): string indicating the path to the file.
        file_data (list): a list of strings to be written into the file.
    """
    with open(filename, 'w') as file:
        file.writelines(file_data)
