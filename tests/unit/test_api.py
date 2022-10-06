import pytest
from pyGeckoCrypto import request, check_coinID, check_currency, check_timestamp
from pyGeckoCrypto.custom_exception import InvalidRequestException

good_URL_data = [
    ("https://api.coingecko.com/api/v3/coins/list", list),
    ("https://api.coingecko.com/api/v3/simple/supported_vs_currencies", list),
    (
        "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd",
        dict,
    ),
]

bad_URL_data = [
    ("https://api.c0ingeck0.com/api/v3/coin/"),
    ("https://ap1.coingecko.com/api/v3/simple/supported_vs_currencies"),
    ("https://api.coingecko.ORG/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"),
    ("https://apiS.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"),
]

coinID_test_data = [
    ("bitcoin", True),
    ("ethereum", True),
    ("fantom", True),
    ("gmx", True),
    ("optimism", True),
    ("btc", False),
    ("eth", False),
    ("ftm", False),
    ("op", False),
]

currency_test_data = [
    ("btc", True),
    ("eth", True),
    ("usd", True),
    ("inr", True),
    ("usdt", False),
    ("paise", False),
    ("dollar", False),
    ("bitcoin", False),
]

timestamp_test_data = [
    ("1665051578", True),
    ("1664582400", True),
    ("1234", True),
    ("12345678", True),
    ("123456789000", False),
    ("abcd", False),
    ("123O", False),
    ("1234-5678", False),
]


@pytest.mark.parametrize("URL, response", good_URL_data)
def test_request_pass(URL, response):
    assert type(request(URL)) == response


@pytest.mark.parametrize("URL", bad_URL_data)
def test_request_fail(URL):
    with pytest.raises(InvalidRequestException):
        request(URL)


@pytest.mark.parametrize("coinID, response", coinID_test_data)
def test_check_coinID(coinID, response):
    assert check_coinID(coinID) == response


@pytest.mark.parametrize("currency, response", currency_test_data)
def test_check_currency(currency, response):
    assert check_currency(currency) == response

@pytest.mark.parametrize("timestamp, response", timestamp_test_data)
def test_check_timestamp(timestamp, response):
    assert check_timestamp(timestamp) == response
