import pytest
from exchange.gemini import Gemini

@pytest.fixture
def gemini():
    return Gemini()

def test_get_amount_invested(gemini):
    assert gemini.get_amount_invested() == 0

