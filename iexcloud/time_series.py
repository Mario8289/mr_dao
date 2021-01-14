from typing import AnyStr

import logging
from pandas import DataFrame

from dao.iexcloud.base import IEXBase


class TimeSeries(IEXBase):
    def __init__(self, sandbox_view: bool = False):
        super().__init__(sandbox_view=sandbox_view)
        self.dataset = "fundamentals"
        self.group = "time-series"
        self.logger = logging.getLogger("AdvancedFundamentals")

    def get_advanced_fundamentals(self, symbol: AnyStr, period: AnyStr = None):

        query_parameters: str = self.get_query_parameters()

        api_call: str = f"{self.base_url}/{self.version}/{self.group}/{self.dataset}/{symbol}/{period}{query_parameters}"

        self.logger.info(f"API Call: {api_call}")

        data = self.get_json(api_call)
        return DataFrame(data)


if __name__ == "__main__":
    time_series = TimeSeries(sandbox_view=True)
    df = time_series.get_advanced_fundamentals("AAPL", period="quarterly")  # "annual" | "quarterly
    print("we have a dataframe people!")



