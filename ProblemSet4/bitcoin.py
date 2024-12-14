"""
Problem Set 4
Program: Bitcoin Price Index
Author: Alexis Varas Ortiz
"""

import sys
import requests


def main():
    # Validate command-line argument is a number
    try:
        buy = float(sys.argv[1])
    # Handle exception in case argument is non-numeric or does not exist
    except ValueError:
        print("Command-line argument is not a number")
    except IndexError:
        print("Missing command-line argument")

    # Retrieve bitcoin price information from coindesk and parse it to json
    try:
        response = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json"
        ).json()
    except (requests.RequestException, requests.ConnectionError, requests.Timeout):
        print("Something went wrong.")
        sys.exit(0)

    bitcoin_value = response["bpi"]["USD"]["rate_float"]

    print(f"${buy * bitcoin_value:,.4f}")

    sys.exit()


if __name__ == "__main__":
    main()
