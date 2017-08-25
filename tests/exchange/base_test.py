import pytest
from exchange.base import DummyExchange


@pytest.fixture
def exchange():
    return DummyExchange()


def test_get_amount_invested(exchange):
    assert exchange.get_amount_invested() == 0
