from typing import AnyStr, List
import pandas as pd

from cryptowatch.base import CyptoWatchBase


class Markets(CyptoWatchBase):
    def __init__(self):
        self.group = 'markets'

    def period_to_seconds(self, periods: List[AnyStr]) -> AnyStr:
        mapping = {
            "1m": 60,
            "1h": 3600
        }
        return ','.join(map(lambda x: str(mapping.get(x)), periods))

    def ohlc(
            self,
            exchange: AnyStr,
            pair: AnyStr,
            before: int = None,
            after: int = None,
            periods: List[AnyStr] = None) -> pd.DataFrame:
        columns = ['close_time', 'open_price', 'high_price', 'low_price', 'close_price', 'volume', 'quote_volume']

        periods = self.period_to_seconds(periods)
        optional_params: str = self.get_optional_parameters(before=before, after=after, periods=periods)
        api_call: str = f"{self._URL}/{self.group}/{exchange}/{pair}/ohlc?{optional_params}"
        result = self.get_json(api_call)

        df = pd.DataFrame(columns=columns)
        for period in periods.split(','):
            df_period = pd.DataFrame(result['result'][period], columns=columns)
            df_period['period'] = int(period)
            df = pd.concat([df, df_period])

        return df


if __name__ == '__main__':
    cry = Markets()
    df = cry.ohlc(exchange='binance', pair='btcusdt', after=162282010, periods=['1m', '1h'])