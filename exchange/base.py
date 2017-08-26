from abc import ABCMeta
from abc import abstractmethod
from abc import abstractproperty


class AbstractExchange(metaclass=ABCMeta):

    @abstractproperty
    def exchange_uri(self):
        pass

    @abstractproperty
    def exchange(self):
        pass

    @abstractmethod
    def get_portfolio_value(self, asset=None):
        """
        Gets the portfolio value associated with the `api_key` under `self.exchange` in
        the `exchanges.yaml` file. This function recognizes assets
        withdrawn from this exchange to wallets in the `wallets` list as owned
        assets, meaning these assets will count towards your total portfolio
        value.

        Args:
            asset(exchange.constants.Asset): If provided will only return portfolio
                value for the given asset. Otherwise value derived from all assets
                on the exchange will be returned.

        Returns:
            int: Representing net portfolio value
        """
        pass


class DummyExchange(AbstractExchange):

    def get_amount_invested(self):
        return 0
