import pytest
from exchange.bittrex import BittrexExchange


@pytest.fixture
def bittrex_exchange():
    return BittrexExchange()


def test_get_amount_invested(bittrex_exchange):
    assert bittrex_exchange.get_amount_invested() == 0
