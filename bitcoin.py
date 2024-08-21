import sys
import requests
import json

if len(sys.argv) != 2:
        print("Missing commander Line!")
else:    
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")    


try:
        float(sys.argv[1])   
    #json.dumps(response.json(), indent=2
        
except ValueError:
        print("Command-line argument is not a number")
     

data = response.json()
bpi = data["bpi"]#["USD"]["rate"]
usd = bpi["USD"]
price = usd["rate"]
price = price.replace(",","")
price = float(price) * float(sys.argv[1])
print(f"${price:,.4f}")
    