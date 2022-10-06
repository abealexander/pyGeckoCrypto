# API Reference

## Getting Current Price

??? note "Example"
    ### Short Example
    ```python
    from pyGeckoCrypto import get_current_price
    coinID = "bitcoin"
    currency = "usd"
    get_current_price(coinID, currency)
    ```

| Args   | Type | Description | 
|:--------:|:------:|:-------|
| coinID    | str | input coin name as per API id as a string |
| currency | str | input currency as a string |

| Returns   |Type | Description | 
|:--------:|:--------:|:-----|
| Response    |  float   | returns price of the coin |


## Getting Historical Price for a period

??? note "Example"
    ### Short Example
    ```python
    from pyGeckoCrypto import get_hist_price_range
    coinID = "bitcoin"
    currency = "usd"
    startdate = "1625097600"
    enddate = "1627775999"
    get_hist_price_range(coinID, currency, startdate, enddate)
    ```

| Args   | Type | Description | 
|:--------:|:------:|:-------|
| coinID    | str | input coin name as per API id as a string |
| currency | str | input currency as a string |
| startdate   | str | input start date in UNIX Time as a string |
| enddate | str | input start date in UNIX Time as a string |

| Returns   |Type | Description | 
|:--------:|:--------:|:-----|
| Response    |  dict   | returns historical price for the period |