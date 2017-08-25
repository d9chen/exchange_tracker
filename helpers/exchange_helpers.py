import os


class InvalidDirectoryError(Exception):
    pass


class FileNotFoundError(Exception):
    pass


def search_for_exchanges_yaml(directory, target=None):
    """Naively looks 'upwards' for 'target'. Starts searching from
    directory pointed to by 'directory', if not found there then
    traverses up one directory and looks again there etc..

    Args:
        directory(str): Represents a directory in the current filesystem.
            eg: '/usr/lib'

        target(str): Search target, if not provided then defaults to exchanges.yaml

    Returns:
        str: Representing the absolute path to the 'exchanges.yaml' file

    Raises:
        InvalidDirectoryError: If 'directory' is not a valid directory on the
            filesystem.
        FileNotFoundError: If 'target' cannot be found.
    """
    target = target or 'exchanges.yaml'
    if not os.path.isdir(directory):
        raise InvalidDirectoryError

    potential_file_path = os.path.abspath(os.path.join(directory, target))

    while not os.path.isfile(potential_file_path):
        directory = os.path.abspath(os.path.join(directory, ".."))
        potential_file_path = os.path.abspath(os.path.join(directory, target))

        if directory == os.path.abspath(os.path.join(directory, "..")):
            # Reached, and searched root dir. Can't locate target
            raise FileNotFoundError

    return potential_file_path
