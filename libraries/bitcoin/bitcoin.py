
import sys

import requests
def main():
    if len(sys.argv)!=2:
        sys.exit("Missing command-line argument")

    try:

        number=float(sys.argv[1])

    except ValueError:
        sys.exit("Command-line argument is not a number")
      

   
    try:
        response=requests.get( "https://rest.coincap.io/v3/assets/bitcoin?apiKey=63959ff1066adebf935317febcebeeb22ea98cd69047f1c5608987475b7f120a")
        response.raise_for_status()
    except (requests.RequestException):
        sys.exit("Could'nt get requests")
      
 
    data=response.json()

    for keys,values in data['data'].items():
        if keys=='priceUsd':
            store_value=float(values)
            break
            
    cal=store_value * number

    print(f"${cal:,.4f}")
        
            

main()