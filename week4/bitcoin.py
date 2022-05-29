# CLI argv of # of bitcoins n
# if cannot be converted to a float; sys.exit() with err message
# query https://api.coindesk.com/v1/bpi/currentprice.json for current price of bitcoin as a float
# output current cost of n bitcoins to four decimal places with , (thousands seperator)
# 4 decimal places formatting, print(f"${amount:,.4f}")

import requests
import sys
import json

try:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")
    elif (len(sys.argv) > 1 ):
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        output = response.json()

        rateFloat = output["bpi"]["USD"]['rate_float']

        perCoin = rateFloat * float(sys.argv[1])
        print(f"${perCoin:,.4f}")

except requests.RequestException:
    sys.exit()
