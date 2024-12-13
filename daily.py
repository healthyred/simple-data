import requests
import json
from datetime import datetime

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
    data = response.json()['prices']

    with open(text_file, mode="w", encoding="utf-8") as file:
        # Write the data as plain text or JSON-formatted string
        if data:
            file.write(str(data))  # Convert the data to a string and save it
        else:
            file.write("No data available to save.")
    print(f"Data has been saved to {text_file}")

def read_prices_from_file(file_name):
    try:
        with open(file_name, mode="r", encoding="utf-8") as file:
            # Read the content of the file
            content = file.read()

            # Use json.loads to parse the array
            array = json.loads(content.replace("'", '"'))
            return array
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def get_price_summary():
    coin_price_data = read_prices_from_file('price.txt')
    profit_loss_data = read_prices_from_file('data.txt')

    total_pnl = 0
    for day_pnl in profit_loss_data:
        current_day = day_pnl[0]
        date_object = datetime.strptime(current_day, "%m/%d/%Y")
        target_timestamp = int(date_object.timestamp()) * 1000
        
        # Initialize variables to store the closest timestamp and price
        closest_price = None
        closest_timestamp = None
        smallest_diff = float('inf')  # Start with a very large difference
        previous_diff = float('inf')

        # Iterate over the list of coin prices
        for timestamp, price in coin_price_data:
            diff = abs(target_timestamp - timestamp)  # Calculate absolute difference
            if diff < smallest_diff:  # Update if a smaller difference is found
                smallest_diff = diff
                previous_diff = diff
                closest_timestamp = timestamp
                closest_price = price
            if diff > previous_diff:
                break

        # print(closest_price)
        # Convert the day to a timestamp

        pnl = int(day_pnl[1])
        total_pnl += float(pnl) * float(closest_price)

    print(total_pnl/ 1000000000)

    
    # matt = [['a', 1], ['b', 2], ['c', 3]]
    # print(matt[2][1])

    # for i in range(len(coin_price_data)):
    #     # print(i)
    #     print(coin_price_data[i][0])

    # for day in coin_price_data:
    #     print(day)
    #     print()




if __name__ == '__main__':
    get_price_summary()