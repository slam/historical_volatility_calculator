# Historical Volatility Calculator

This Python script calculates the historical volatility of ETFs over multiple time periods (1-year, 3-year, and 5-year). It uses daily return data to compute annualized volatility for a predefined list of Vanguard ETFs.

## Features

- Fetches historical price data using the yfinance library with improved reliability
- Calculates annualized volatility for 1-year, 3-year, and 5-year periods
- Includes retry logic with exponential backoff for handling rate limits
- Provides progress indicators during processing
- Outputs results in a tab-separated format for easy copying into spreadsheets

## Requirements

- Python 3.6+
- yfinance
- pandas
- numpy

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/slam/historical_volatility_calculator.git
   cd historical_volatility_calculator
   ```

2. Install the required packages:
   ```
   uv pip install yfinance pandas numpy
   ```

## Usage

1. Run the script:
   ```
   uv run historical_volatility_calculator.py
   ```

2. The script will:
   - Process 24 predefined Vanguard ETFs (equity and bond funds)
   - Show progress as it fetches data for each ETF
   - Automatically handle rate limiting with retry logic
   - Output a tab-separated table with volatility results

3. Copy the output table into your preferred spreadsheet application.

## Sample Output

```
Processing BNDW (1/24)...
Processing BNDX (2/24)...
...

ETF     1Y Volatility    3Y Volatility    5Y Volatility
BNDW    0.065432         0.072341         0.068765
VOO     0.152341         0.187654         0.201234
VYM     0.141256         0.165432         0.178901
...
```

## Included ETFs

The script analyzes the following Vanguard ETFs:

**Equity ETFs:**
- VT (Total World Stock)
- VOO (S&P 500)
- VYM (High Dividend Yield)
- VIG (Dividend Appreciation)
- VTV (Value)
- VBR (Small-Cap Value)
- VEA (Developed Markets)
- VEU (All-World ex-US)
- VYMI (International High Dividend)
- VIGI (International Dividend Growth)
- VWO (Emerging Markets)
- VPL (Pacific)
- VGK (European)

**Bond ETFs:**
- BNDW (World Bond)
- BNDX (International Bond)
- VWOB (Emerging Markets Government Bond)
- VTES (Tax-Exempt Bond)
- VCSH (Short-Term Corporate Bond)
- VGIT (Intermediate-Term Treasury)
- VTEB (Tax-Exempt Bond)
- VGSH (Short-Term Treasury)
- VGLT (Long-Term Treasury)
- VCIT (Intermediate-Term Corporate Bond)
- VTIP (Short-Term Inflation-Protected Securities)

## Technical Details

- Uses 252 trading days for annualization (standard for US markets)
- Implements exponential backoff retry logic for API rate limits
- Adds 1-second delay between ticker requests to prevent rate limiting
- Requires minimum data points (252 days) for volatility calculation
- Empty or missing data periods are handled gracefully

## License

[MIT](https://choosealicense.com/licenses/mit/)
