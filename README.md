# Multi-Period Volatility Calculator

This Python script calculates the historical volatility of stocks, ETFs, and
other tradable securities over multiple time periods (1-year, 3-year, and
5-year). It uses daily return data to compute annualized volatility for a list
of specified ticker symbols.

## Features

- Fetches historical price data for any ticker symbol using the yfinance library
- Calculates annualized volatility for 1-year, 3-year, and 5-year periods
- Outputs results in a format easy to copy into spreadsheet software

## Requirements

- Python 3.6+
- yfinance
- pandas
- numpy

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/slam/multi-period-volatility.git
   cd multi-period-volatility
   ```

2. Install the required packages:
   ```
   uv pip install yfinance pandas numpy
   ```

## Usage

1. Open the script and modify the `tickers` list to include the symbols you
   want to analyze.

2. Run the script:
   ```
   uv run multi_period_volatility.py
   ```

3. The script will output a tab-separated table with the volatility results for
   each ticker, which can be easily copied into a spreadsheet.

## Sample Output

```
Ticker  1Y Volatility    3Y Volatility    5Y Volatility
AAPL    0.123456         0.234567         0.345678
GOOGL   0.234567         0.345678         0.456789
SPY     0.345678         0.456789         0.567890
...
```

## Notes

- The script uses 252 trading days for annualization, which is standard for US
  markets. Adjust if using for other markets.
- Ensure you have a stable internet connection, as the script fetches data
  online.
- Some securities may not have a full 5 years of historical data, which may
  affect calculations.
- The script can handle stocks, ETFs, and other securities available through
  Yahoo Finance.

## License

[MIT](https://choosealicense.com/licenses/mit/)
