import requests

def main():
    # List of cryptocurrencies you want to track
    crypto_symbols = ["bitcoin", "ethereum", "cardano", "ripple", "litecoin", "polkadot", "solana", "uniswap",
                      "dogecoin", "polygon"]

    # Fetch data
    crypto_data = fetch_crypto_data(crypto_symbols)
    
    # If data is successfully fetched, process and display it
    if crypto_data:
        performance_data = process_crypto_data(crypto_data)
        display_performance(performance_data)
        compare_performance(performance_data)

def fetch_crypto_data(crypto_symbols):
    """
    Fetches real-time cryptocurrency data from CoinGecko API.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",  # Fetch prices in USD
        "ids": ",".join(crypto_symbols),  # Comma-separated list of crypto IDs
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "price_change_percentage": "24h"  # Include 24-hour percentage change
    }

    # Send the request to the CoinGecko API
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()  # Return the API response as a JSON object
    else:
        print("Failed to fetch data from CoinGecko API")
        return []

def process_crypto_data(crypto_data):
    """
    Extracts relevant information from the fetched data and formats it.
    """
    performance_data = []
    for crypto in crypto_data:
        symbol = crypto["symbol"].upper()
        price = crypto["current_price"]
        change_24h = crypto["price_change_percentage_24h"]

        # Store relevant data in a list of dictionaries
        performance_data.append({
            "symbol": symbol,
            "price": price,
            "24h_change": change_24h
        })

    return performance_data

def display_performance(performance_data):
    """
    Displays the cryptocurrency performance data in a tabular format.
    """
    print(f"{'Symbol':<10} {'Price (USD)':<15} {'24h Change (%)':<15}")
    print("-" * 40)
    
    for data in performance_data:
        print(f"{data['symbol']:<10} {data['price']:<15.2f} {data['24h_change']:<15.2f}")

def compare_performance(performance_data):
    """
    Compares and prints the best and worst performing cryptocurrencies based on 24h change.
    """
    best_performer = max(performance_data, key=lambda x: x["24h_change"])
    worst_performer = min(performance_data, key=lambda x: x["24h_change"])

    print(f"\nBest performer: {best_performer['symbol']} with {best_performer['24h_change']:.2f}% change")
    print(f"Worst performer: {worst_performer['symbol']} with {worst_performer['24h_change']:.2f}% change")

if __name__ == "__main__":
    main()
