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

# Subscribe to live news updates
ib.reqMktData(contract, 'mdoff,292:BZ', False, False)

# Define a function to handle the news updates
def news_handler(msg):
    print(f"News headline: {msg.headline}")

# Register the news handler function with the ib_insync event loop
ib.pendingTickersEvent += news_handler

# Run the ib_insync event loop indefinitely
ib.run()

# Disconnect when done
ib.disconnect()
