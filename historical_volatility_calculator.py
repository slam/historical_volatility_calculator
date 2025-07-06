import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time


def calculate_volatility(returns, trading_days=252):
    if len(returns) < trading_days:
        return None
    return returns.std() * np.sqrt(trading_days)


def get_etf_data(ticker, end_date, years, retry_count=3):
    start_date = (
        datetime.strptime(end_date, "%Y-%m-%d") - timedelta(days=years * 365)
    ).strftime("%Y-%m-%d")
    
    for attempt in range(retry_count):
        try:
            # Use yf.download instead of Ticker.history for better reliability
            hist = yf.download(ticker, start=start_date, end=end_date, 
                             progress=False, auto_adjust=True, 
                             prepost=False, threads=False)
            
            if hist.empty:
                print(f"{ticker}: No data available for period {start_date} to {end_date}")
                return None
                
            # Calculate daily returns
            hist["Daily Return"] = hist["Close"].pct_change()
            return hist
            
        except Exception as e:
            if "429" in str(e) or "Too Many Requests" in str(e):
                wait_time = (attempt + 1) * 2  # Exponential backoff
                print(f"{ticker}: Rate limited, waiting {wait_time}s... (attempt {attempt + 1}/{retry_count})")
                time.sleep(wait_time)
            else:
                print(f"{ticker}: Error - {str(e)}")
                return None
    
    print(f"{ticker}: Failed after {retry_count} attempts")
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
        "VGIT",
        "VTEB",
        "VGSH",
        "VGLT",
        "VCIT",
        "VTIP",
    ]
    end_date = datetime.now().strftime("%Y-%m-%d")

    results = {}
    for i, etf in enumerate(etfs):
        print(f"Processing {etf} ({i+1}/{len(etfs)})...")
        volatilities = calculate_volatilities(etf, end_date)
        if volatilities:
            results[etf] = volatilities
        
        # Add delay between tickers to avoid rate limiting
        if i < len(etfs) - 1:  # Don't sleep after the last ticker
            time.sleep(1)

    # Print results in a format easy to copy into Google Sheets
    if results:
        print("\nETF\t1Y Volatility\t3Y Volatility\t5Y Volatility")
        for etf, vols in results.items():
            vol_str = [f"{v:.6f}" if v is not None else "" for v in vols]
            print(f"{etf}\t{vol_str[0]}\t{vol_str[1]}\t{vol_str[2]}")
    else:
        print("\nNo data retrieved for any ETFs. Please check your internet connection and try again.")


if __name__ == "__main__":
    main()
