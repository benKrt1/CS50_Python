import requests
import sys

def main():
    try:
        btc = get_btc()
        if len(sys.argv) == 2:
            piece_btc = float(sys.argv[1])
            price = btc * piece_btc
            print(f"${price:,.4f}")
        else:
            raise IndexError
    except ValueError:
        sys.exit("Not a number")
    except IndexError:
        sys.exit("Missing a command-line argument")
    except requests.RequestException:
        sys.exit("Could not get Bitcoin price")
    return btc


def get_btc():
    link = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=32a7f29dac051feec5ceca956fd3c81fae93e8fdc497faa819613bd7a9d83279"
    api = requests.get(link)

    coin = api.json()
    price_btc = float(coin["data"]["priceUsd"])
    return price_btc   


if __name__ == "__main__":
    main()