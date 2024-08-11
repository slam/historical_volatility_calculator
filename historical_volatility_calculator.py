import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def calculate_volatility(returns, trading_days=252):
    if len(returns) < trading_days:
        return None
    return returns.std() * np.sqrt(trading_days)


def get_etf_data(ticker, end_date, years):
    start_date = (
        datetime.strptime(end_date, "%Y-%m-%d") - timedelta(days=years * 365)
    ).strftime("%Y-%m-%d")
    try:
        etf = yf.Ticker(ticker)
        hist = etf.history(start=start_date, end=end_date)
        if hist.empty:
            return None
        hist["Daily Return"] = hist["Close"].pct_change()
        return hist
    except Exception as e:
        print(f"Error fetching data for {ticker}: {str(e)}")
        return None


def calculate_volatilities(ticker, end_date):
    data = get_etf_data(ticker, end_date, 5)  # Get 5 years of data
    if data is None:
        return None

    vol_1y = calculate_volatility(data["Daily Return"].iloc[-252:])
    vol_3y = calculate_volatility(data["Daily Return"].iloc[-756:])
    vol_5y = calculate_volatility(data["Daily Return"])

    return vol_1y, vol_3y, vol_5y


def main():
    etfs = [
        "BNDW",
        "BNDX",
        "VWOB",
        "VTES",
        "VCSH",
        "VT",
        "VOO",
        "VYM",
        "VIG",
        "VTV",
        "VBR",
        "VEA",
        "VEU",
        "VYMI",
        "VIGI",
        "VWO",
        "VPL",
        "VGK",
    ]
    end_date = datetime.now().strftime("%Y-%m-%d")

    results = {}
    for etf in etfs:
        volatilities = calculate_volatilities(etf, end_date)
        if volatilities:
            results[etf] = volatilities

    # Print results in a format easy to copy into Google Sheets
    print("ETF\t1Y Volatility\t3Y Volatility\t5Y Volatility")
    for etf, vols in results.items():
        vol_str = [f"{v:.6f}" if v is not None else "" for v in vols]
        print(f"{etf}\t{vol_str[0]}\t{vol_str[1]}\t{vol_str[2]}")


if __name__ == "__main__":
    main()
