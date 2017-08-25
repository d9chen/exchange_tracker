import pytest
import random
import string
from helpers.exchange_helpers import FileNotFoundError
from helpers import exchange_helpers


def generate_random_string(n=8):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))


def test_exchange_helpers_raises_when_file_not_found_on_root():
    with pytest.raises(FileNotFoundError):
        exchange_helpers.search_for_exchanges_yaml(
            '/', generate_random_string())