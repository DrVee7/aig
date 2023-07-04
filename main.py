from ib_insync import *
import time
from datetime import datetime

def nearest_expiry():
    current_month = datetime.now().month
    current_year = datetime.now().year
    contract_months = [3, 6, 9, 12]
    expiry_month = next((month for month in contract_months if month >= current_month), contract_months[0])
    if expiry_month < current_month:
        current_year += 1
    return f'{current_year}{expiry_month:02}'

try:
    ib = IB()
    ib.connect('127.0.0.1', 7497, clientId=1)
except Exception as e:
    print("Error connecting to IB: ", e)
    exit()

contract = Future('ES', nearest_expiry(), 'CME')
ib.reqMarketDataType(3)

upper_limit = 4300  
lower_limit = 4270.5

while True:
    try:
        [ticker] = ib.reqTickers(contract)
        # Print the current price
        print(f"Current price: {ticker.marketPrice()}")
    except Exception as e:
        print("Error getting market data: ", e)
        break  # Or: continue

    try:
        current_price = ticker.marketPrice()
        if current_price >= upper_limit:
            order = LimitOrder('SELL', 100, upper_limit)
            trade = ib.placeOrder(contract, order)
            print(f"Placed SELL order at limit price: {upper_limit}")
        elif current_price <= lower_limit:
            order = LimitOrder('BUY', 300, lower_limit)
            trade = ib.placeOrder(contract, order)
            print(f"Placed BUY order at limit price: {lower_limit}")
    except Exception as e:
        print("Error placing order: ", e)

    time.sleep(5)

try:
    ib.disconnect()
except Exception as e:
    print("Error disconnecting from IB: ", e)
