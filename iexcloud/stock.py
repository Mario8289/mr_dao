from typing import AnyStr

import logging
from pandas import DataFrame

from dao.iexcloud.base import IEXBase


class Stock(IEXBase):
    def __init__(self, sandbox_view: bool = False):
        super().__init__(sandbox_view=sandbox_view)
        self.group = "stock"
        self.logger = logging.getLogger("Stock")

    def get_balance_sheet(self, symbol: AnyStr, period: AnyStr = None, last: int = None):
        query_parameters: str = self.get_query_parameters(period=period, last=last)

        api_call: str = f"{self.base_url}/{self.version}/{self.group}/{symbol}/balance-sheet{query_parameters}"

        self.logger.info(f"API Call: {api_call}")

        data = self.get_json(api_call)
        return DataFrame(data['balancesheet'])

    def get_cashflow(self, symbol: AnyStr, period: AnyStr = None, last: int = None):
        query_parameters: str = self.get_query_parameters(period=period, last=last)

        api_call: str = f"{self.base_url}/{self.version}/{self.group}/{symbol}/cash-flow{query_parameters}"

        self.logger.info(f"API Call: {api_call}")

        data = self.get_json(api_call)
        return DataFrame(data["cashflow"])

    def get_financials(self, symbol: AnyStr, period: AnyStr = None, last: int = None):
        query_parameters: str = self.get_query_parameters(period=period, last=last)

        api_call: str = f"{self.base_url}/{self.version}/{self.group}/{symbol}/financials{query_parameters}"

        self.logger.info(f"API Call: {api_call}")

        data = self.get_json(api_call)
        return DataFrame(data["financials"])

    def get_income_statement(self, symbol: AnyStr, period: AnyStr = None, last: int = None):

        query_parameters: str = self.get_query_parameters(period=period, last=last)

        api_call: str = f"{self.base_url}/{self.version}/{self.group}/{symbol}/income{query_parameters}"

        self.logger.info(f"API Call: {api_call}")

        data = self.get_json(api_call)
        return DataFrame(data["income"])


if __name__ == "__main__":
    stock = Stock(sandbox_view=True)
    df = stock.get_balance_sheet("AAPL", period="quarter", last=12)
    print("we have a dataframe people!")