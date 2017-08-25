from exchange.base import AbstractExchange


class BittrexExchange(AbstractExchange):
    """Bittrex client used to interface with the Bittrex API. Documentation
    available at https://bittrex.com/Home/Api.
    """

    EXCHANGE_URI = "https://bittrex.com/api/{version}/{method}"

    def __init__(self, version='v1.1'):
        """
        Args:
            version (str): Version of Bittrex API to target calls against.
        """
        self.version = version
        self._load_api_key_and_secret()

    def get_amount_invested(self):
        return 0

    def _generate_request_uri(self, method):
        """Generates an URI to target request against

        Args:
            method (str): The particular method to generate an URI for
        """

        return self.EXCHANGE_URI.format(version=self.version, method=method)

    def _load_api_key_and_secret(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))

