# app/robo_advisor.py


# INFO INPUTS

import requests
import json
import datetime

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

latest_close = parsed_response["Time Series (Daily)"]["2020-06-10"]["4. close"]

def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71


# INFO OUTPUTS

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: " + (current_time))
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")