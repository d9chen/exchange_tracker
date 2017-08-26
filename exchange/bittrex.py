import hashlib
import hmac
import urllib.parse

import requests

from exchange.base import AbstractExchange
from exchange.constants import ExchangeConstant
from helpers import exchange_helpers


class BittrexExchange(AbstractExchange):
    """Bittrex client used to interface with the Bittrex API. Documentation
    available at https://bittrex.com/Home/Api.
    """

    def __init__(self, api_key=None, api_secret=None, version='v1.1'):
        """
        Args:
            version (str): Version of Bittrex API to target calls against.
        """
        self.version = version
        if not api_key or not api_secret:
            self._load_api_key_and_secret()

    @property
    def exchange_uri(self):
        return "https://bittrex.com/api/{version}/{method}/{resource}?"

    @property
    def exchange(self):
        return ExchangeConstant.BITTREX

    def get_portfolio_value(self, asset=None):
        return 0

    def _query_api(self, method, resource):
        """Generates an URI to target request against

        Args:
            method (str): The particular method to generate an URI for
        """
        uri = self.exchange_uri.format(
            version=self.version,
            method=method,
            resource=resource
        )
        params = {'apikey': self._api_creds.key}
        uri = uri + urllib.parse.urlencode(params)

        api_sign = hmac.new(
            self._api_creds.secret.encode(),
            uri.encode(),
            hashlib.sha512
        ).hexdigest()

        return requests.get(uri, headers={'apisign': api_sign})

    def _load_api_key_and_secret(self):
        self._api_creds = exchange_helpers.get_exchange_api_creds(
            self.exchange)
