# Approach
For this particular task, I took a beginner's approach. I acquired some foundational knowledge about options trading from Investopedia and familiarized myself with the operation of calls and puts. Subsequently, I wrote a script to execute a series of trades.

# Assumptions
The Federal Meeting held on June 14, 2023, maintained steady rates and paused its rate-hiking campaign. This was in line with market expectations, resulting in a bullish market sentiment. Investors were not disappointed, as the latest Summary of Economic Projections from the Fed indicates upcoming rate hikes. However, this project remains unaffected as the next Federal Meeting is scheduled for July 26, 2023. 

# Code
## main.py
The main.py runs and displays the real-time price, as shown below. Additionally, I have the ability to specify the number of contracts I intend to purchase and set a target buying price. In the case of this particular contract, I placed a buy order with a limit price of 4270.5.

```bash
Current price: 4272.0
Current price: 4272.0
Current price: 4271.75
Current price: 4271.75
Current price: 4270.0
Placed BUY order at limit price: 4270.5
```
## news.py 
The news.py connects to Interactive Brokerage live news updates and prints the news headlines. However, it didn't work as expected beacuse they required subscription. 

The error message is as follows. 

```bash
Error 10168, reqId 15: Requested market data is not subscribed. Delayed market data is not enabled., contract: Future(symbol='ES' lastTradeDateOrContractMonth='202306', exchange='CME')
```

# Trading History
The initial account I created consistently presented error messages, leading me to create a new account. The image below illustrates my successful automatic purchase of a contract on June 5th for $4,288.00, with the closing price for that day being $4,281.00. At the outset, the platform experienced frequent crashes, hindering my access to the complete transaction history.
![history](https://github.com/drvee7/aig/blob/main/history.png "history")


