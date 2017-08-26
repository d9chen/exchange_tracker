import pytest

from exchange.bittrex import BittrexExchange


@pytest.fixture
def bittrex_exchange():
    return BittrexExchange(api_key='dummy_key', api_secret='dummy_secret')


def test_get_amount_invested(bittrex_exchange):
    assert bittrex_exchange.get_portfolio_value() == 0
