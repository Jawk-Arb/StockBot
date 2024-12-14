import yfinance as yf

def get_stock_info(ticker):
    try:
        # Create Ticker object
        stock = yf.Ticker(ticker)
        info = stock.info
        
        # Extract and format key information
        stock_data = {
            "Company Name": info.get("longName", "N/A"),
            "Current Price": info.get("currentPrice", "N/A"),
            "Market Cap": info.get("marketCap", "N/A"),
            "P/E Ratio": info.get("trailingPE", "N/A"),
            "EPS": info.get("trailingEps", "N/A"),
            "52 Week High": info.get("fiftyTwoWeekHigh", "N/A"),
            "52 Week Low": info.get("fiftyTwoWeekLow", "N/A"),
            "Sector": info.get("sector", "N/A"),
            "Industry": info.get("industry", "N/A"),
            "Dividend Yield": info.get("dividendYield", "N/A"),
        }
        
        # Print information in a formatted way
        print("\nStock Information:")
        print("-" * 50)
        for key, value in stock_data.items():
            print(f"{key}: {value}")
            
    except Exception as e:
        print(f"Error fetching data: {e}")

def main():
    while True:
        # Get user input
        ticker = input("\nEnter stock ticker (or 'quit' to exit): ").strip().upper()
        
        if ticker.lower() == 'quit':
            print("Goodbye!")
            break
            
        if ticker:
            print(f"\nFetching data for {ticker}...")
            get_stock_info(ticker)
        else:
            print("Please enter a valid ticker.")

if __name__ == "__main__":
    main()
