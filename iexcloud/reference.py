from typing import AnyStr

import logging
from pandas import DataFrame

from iexcloud.base import IEXBase


class Reference(IEXBase):
    def __init__(self, sandbox_view: bool = False):
        super().__init__(sandbox_view=sandbox_view)
        self.group = "ref-data"
        self.logger = logging.getLogger("Reference")

    def get_international_symbols(self, exchange: AnyStr):
        query_parameters: str = self.get_query_parameters()

        api_call: str = f"{self.base_url}/{self.version}/{self.group}/exchange/{exchange.lower()}/" \
                        f"symbols{query_parameters}"
        self.logger.info(f"API Call: {api_call}")

        data = self.get_json(api_call)

        return DataFrame(data)

    def get_us_symbols(self):

        query_parameters: str = self.get_query_parameters()

        api_call: str = f"{self.base_url}/{self.version}/{self.group}/symbols{query_parameters}"

        self.logger.info(f"API Call: {api_call}")

        data = self.get_json(api_call)

        return DataFrame(data)

    def get_international_exchanges(self):

        query_parameters: str = self.get_query_parameters()

        api_call: str = f"{self.base_url}/{self.version}/{self.group}/exchanges{query_parameters}"

        self.logger.info(f"API Call: {api_call}")

        data = self.get_json(api_call)

        return DataFrame(data)

    def get_us_exchanges(self):

        query_parameters: str = self.get_query_parameters()

        api_call: str = f"{self.base_url}/{self.version}/{self.group}/market/us/exchanges{query_parameters}"

        self.logger.info(f"API Call: {api_call}")

        data = self.get_json(api_call)

        return DataFrame(data)


if __name__ == "__main__":
    ref = Reference(sandbox_view=False)
    df = ref.get_symbols()
    print("we have a dataframe people!")




