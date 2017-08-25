import random
import string
import tempfile

import pytest

from helpers import exchange_helpers
from helpers.exchange_helpers import FileNotFoundError
from helpers.exchange_helpers import InvalidDirectoryError


def generate_random_string(n=8):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))


def test_search_for_exchanges_raises_file_not_found_when_file_not_found_on_root():
    with pytest.raises(FileNotFoundError):
        exchange_helpers.search_for_exchanges_yaml(
            '/', generate_random_string()
        )


def test_search_for_exchanges_raises_invalid_directory_with_invalid_directory():
    with tempfile.TemporaryDirectory() as tmp_dir_name:
        # Creates a temp directory which is deleted once this context ends, so
        # tmp_dir_name is guarenteed to not exist when we use it later on.
        pass

    with pytest.raises(InvalidDirectoryError):
        exchange_helpers.search_for_exchanges_yaml(tmp_dir_name, 'goats')


def test_search_for_exchanges_returns_abs_file_path_when_file_found():
    with tempfile.NamedTemporaryFile() as tmp_file:
        file_name = tmp_file.name.split('/')[-1]
        directory = '/'.join(tmp_file.name.split('/')[:-1])

        assert tmp_file.name == exchange_helpers.search_for_exchanges_yaml(
            directory,
            file_name
        )
