from typing import AnyStr
import requests

from cryptowatch.base import CyptoWatchBase


class Exchanges(CyptoWatchBase):
    def __init__(self):
        pass

    def get_exchanges(self, exchange: str = None):

        api_call: str = f"{self._URL}/exchanges"
        if exchange:
            api_call = f"{api_call}/{exchange}"

        result = requests.get(api_call)

        return result.json()

    def get_pairs(self):
        api_call: str = f"{self._URL}/pairs"

        result = requests.get(api_call)

        return result.json()


if __name__ == '__main__':
    cry = Exchanges()
    #exchange = cry.get_exchanges("binance")
    pairs = cry.get_pairs()
    print(pairs)