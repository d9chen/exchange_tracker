import random
import string
import tempfile

import pytest
import yaml

from exchange.constants import ExchangeConstant
from helpers import exchange_helpers
from helpers.exchange_helpers import FileNotFoundError
from helpers.exchange_helpers import InvalidDirectoryError
from helpers.exchange_helpers import InvalidExchangeError
from helpers.exchange_helpers import MissingExchangeInfoError


@pytest.fixture
def dummy_exchange_data():
    return {
        'bittrex': {'api_key': 'bahh', 'api_secret': 'duhhh'},
        'wallets': ['123'],
    }


def generate_random_string(n=8):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))


def test_search_for_yaml_raises_file_not_found_when_file_not_found_on_root():
    with pytest.raises(FileNotFoundError):
        exchange_helpers.search_for_yaml(
            '/', generate_random_string()
        )


def test_search_for_yaml_raises_invalid_directory_with_invalid_directory():
    with tempfile.TemporaryDirectory() as tmp_dir_name:
        # Creates a temp directory which is deleted once this context ends, so
        # tmp_dir_name is guarenteed to not exist when we use it later on.
        pass

    with pytest.raises(InvalidDirectoryError):
        exchange_helpers.search_for_yaml(tmp_dir_name, 'goats')


def test_search_for_yaml_returns_abs_file_path_when_file_found():
    with tempfile.NamedTemporaryFile() as tmp_file:
        file_name = tmp_file.name.split('/')[-1]
        directory = '/'.join(tmp_file.name.split('/')[:-1])

        assert tmp_file.name == exchange_helpers.search_for_yaml(
            directory,
            file_name
        )


def test_get_exchange_api_creds_raises_with_unrecognized_exchange():
    with pytest.raises(InvalidExchangeError):
        exchange_helpers.get_exchange_api_creds(generate_random_string(n=1))


def test_get_exchange_api_creds_raises_when_exchange_info_missing(
    dummy_exchange_data
):
    with pytest.raises(
        MissingExchangeInfoError
    ), tempfile.NamedTemporaryFile(mode='w') as exchange_details_file:
        yaml.dump(
            dummy_exchange_data,
            exchange_details_file,
            default_flow_style=False
        )
        exchange_details_file.seek(0)

        exchange_helpers.get_exchange_api_creds(
            ExchangeConstant.GEMINI,
            exchange_yaml_path=exchange_details_file.name
        )


def test_get_exchange_api_creds_returns_expected_creds(dummy_exchange_data):
    with tempfile.NamedTemporaryFile(mode='w') as exchange_details_file:
        yaml.dump(
            dummy_exchange_data,
            exchange_details_file,
            default_flow_style=False
        )
        exchange_details_file.seek(0)

        api_cred = exchange_helpers.get_exchange_api_creds(
            ExchangeConstant.BITTREX,
            exchange_yaml_path=exchange_details_file.name
        )

    assert api_cred.key == dummy_exchange_data['bittrex']['api_key']
    assert api_cred.secret == dummy_exchange_data['bittrex']['api_secret']


def test_get_associated_wallets_returns_all_listed_wallets(dummy_exchange_data):
    with tempfile.NamedTemporaryFile(mode='w') as exchange_details_file:
        yaml.dump(
            dummy_exchange_data,
            exchange_details_file,
            default_flow_style=False
        )
        exchange_details_file.seek(0)

        wallets = exchange_helpers.get_associated_wallets(
            exchange_details_file.name
        )

    assert wallets == {*dummy_exchange_data['wallets']}
