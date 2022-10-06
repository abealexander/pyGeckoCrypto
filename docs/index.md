# pyGeckoCrypto

This package is a wrapper of the CoinGecko API which can be used to pull current and historical prices of Crypto Currencies.

- PYPI link for this package - [pyGeckoCrypto](https://pypi.org/project/pyGeckoCrypto)

## Getting Started

### Installation

!!! note "Installation Steps"
    First let's do an easy pip installation of the library by running the following command -
    ```bash
    pip install pyGeckoCrypto
    ```


### Quickstart

```python
# Importing the Package
from pyGeckoCrypto import get_current_price, get_hist_price_range

# Sample Data
coinID = "bitcoin" # Refer Coin List
currency = "usd" # Refer Currency List
startdate = "1625097600" # Unix Timestamp
enddate = "1627775999" # Unix Timestamp

# Getting Current Price
get_current_price(coinID, currency)

# Getting Historical Price for a period
get_hist_price_range(coinID, currency, startdate, enddate)
```
Refer CoinGecko API [doc](https://www.coingecko.com/en/api/documentation) to find more information of the required parameters for the above functions.