import pytest
from pyGeckoCrypto import get_current_price

good_price_data = [
    ("bitcoin", "usd", float),
    ("ethereum", "inr", float),
    ("fantom", "usd", float),
    ("gmx", "cad", float),
    ("optimism", "eur", float),
]

bad_price_data = [("btc", "usd"), ("ethereum", "dollar")]


@pytest.mark.parametrize("coinID, currency, response", good_price_data)
def test_get_current_price_good(coinID, currency, response):
    assert type(get_current_price(coinID, currency)) == response


@pytest.mark.parametrize("coinID, currency", bad_price_data)
def test_get_current_price_bad(coinID, currency):
    with pytest.raises(Exception):
        get_current_price(coinID, currency)
