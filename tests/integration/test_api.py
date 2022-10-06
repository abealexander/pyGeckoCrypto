import pytest
from pyGeckoCrypto import get_current_price, get_hist_price_range

good_price_data = [
    ("bitcoin", "usd", float),
    ("ethereum", "inr", float),
    ("fantom", "usd", float),
    ("gmx", "cad", float),
    ("optimism", "eur", float),
]

bad_price_data = [("btc", "usd"), ("ethereum", "dollar")]

good_price_hist_data = [
    ("bitcoin", "usd", "1664582400", "1665052399", dict),
    ("ethereum", "inr", "1640995200", "1643673599", dict),
    ("fantom", "usd", "1234", "1635724800", dict),
    ("optimism", "eur", "1625097600", "1627775999", dict),
]

bad_price_hist_data = [
    ("btc", "usd", "166458240O", "1665052399"),
    ("ethereum", "dollar", "1640995200", "1643673599"),
    ("fantom", "usd", "1AB234", "1635724800"),
    ("optimism", "eur", "1625097600", "162777--5999"),
]


@pytest.mark.parametrize("coinID, currency, response", good_price_data)
def test_get_current_price_good(coinID, currency, response):
    assert type(get_current_price(coinID, currency)) == response


@pytest.mark.parametrize("coinID, currency", bad_price_data)
def test_get_current_price_bad(coinID, currency):
    with pytest.raises(Exception):
        get_current_price(coinID, currency)


@pytest.mark.parametrize(
    "coinID, currency, startdate, enddate, response", good_price_hist_data
)
def test_get_hist_price_range_good(coinID, currency, startdate, enddate, response):
    assert type(get_hist_price_range(coinID, currency, startdate, enddate)) == response


@pytest.mark.parametrize("coinID, currency, startdate, enddate", bad_price_hist_data)
def test_get_hist_price_range_bad(coinID, currency, startdate, enddate):
    with pytest.raises(Exception):
        get_hist_price_range(coinID, currency, startdate, enddate)
