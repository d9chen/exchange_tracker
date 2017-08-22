import pytest
from exchange.base import Exchange

@pytest.fixture
def exchange():
    return Exchange()

def test_get_amount_invested(exchange):
    assert exchange.get_amount_invested == 0
