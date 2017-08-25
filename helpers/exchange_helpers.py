import os
from collections import namedtuple

import yaml

from exchange.constants import ExchangeConstant


class InvalidDirectoryError(Exception):
    pass


class FileNotFoundError(Exception):
    pass


class InvalidExchangeError(Exception):
    pass


class MissingExchangeInfoError(Exception):
    pass


APICred = namedtuple('APICreds', ['key', 'secret'])


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


def get_exchange_api_creds(exchange, exchange_yaml_path=None):
    """Returns the api key and secret associated with a given exchange

    Args:
        exchange(ExchangeConstant): Exchange to look up creds for.
        exchange_yaml_path(str): Location of a yaml file containing exchange API
            creds.
    Returns:
        APICred: populated with key and secret.

    Raises:
        MissingExchangeInfoError: If exchanges.yaml does not have info for
            the specified `exchange`.
        InvalidExchangeError: if `exchange` is not a member of ExchangeConstant
    """
    try:
        ExchangeConstant(exchange)
    except ValueError:
        raise InvalidExchangeError

    exchange_yaml_path = exchange_yaml_path or search_for_exchanges_yaml(
        os.path.dirname(os.path.realpath(__file__))
    )

    with open(exchange_yaml_path, 'r') as exchange_yaml_file:
        exchanges_dict = yaml.load(exchange_yaml_file)

    if not exchanges_dict:
        raise MissingExchangeInfoError
    elif exchange.value not in exchanges_dict:
        raise MissingExchangeInfoError

    return APICred(
        exchanges_dict[exchange.value]['api_key'],
        exchanges_dict[exchange.value]['api_secret']
    )
