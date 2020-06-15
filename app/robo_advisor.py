# app/robo_advisor.py


# INFO INPUTS

import requests
import json
import datetime
import csv
import os

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey=demo"
response = requests.get(request_url)
# print(type(response)) # class 'requests.models.Response'
# print(response.status_code) # 200
# print(response.text)

parsed_response = json.loads(response.text)



last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

now = datetime.datetime.now()
current_time = (now.strftime("%B %d %Y %I:%M %p"))
print(current_time)

tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys())
latest_day = dates[0]
latest_close = tsd[latest_day]["4. close"]

def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71

high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)

# INFO OUTPUTS

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: " + (current_time))
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")


csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    for date in dates:
        daily_prices = tsd[date]

        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"]
         })
