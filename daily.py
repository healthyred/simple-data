import requests

def main():
    print('hello')

def fetch_and_save():
    url = 'https://doubleupdata.store/unihouse/staker/daily?coin_type=0x2::sui::SUI&staker=0xfd0978a0c4098174ce48b92f5f9411a7826d1d9b3a04e6734e1a34fad7fb6f1b'

    response = requests.get(url)
    data = response.json()
    text_file = "data.txt"

    with open(text_file, mode="w", encoding="utf-8") as file:
        # Write the data as plain text or JSON-formatted string
        if data:
            file.write(str(data))  # Convert the data to a string and save it
        else:
            file.write("No data available to save.")
    print(f"Data has been saved to {text_file}")


def fetch_data_from_coingecko():
    url = "https://api.coingecko.com/api/v3/coins/sui/market_chart/range?vs_currency=usd&from=1725158155&to=1734057355"

    headers = {
        "accept": "application/json",
        "x-cg-api-key": "CG-rXFGnKYzhbCQe1HsL8a2HyA9\t"
    }
    text_file = "price.txt"
    response = requests.get(url, headers=headers)
    data = response.json()
    with open(text_file, mode="w", encoding="utf-8") as file:
        # Write the data as plain text or JSON-formatted string
        if data:
            file.write(str(data))  # Convert the data to a string and save it
        else:
            file.write("No data available to save.")
    print(f"Data has been saved to {text_file}")


if __name__ == '__main__':
    fetch_data_from_coingecko()