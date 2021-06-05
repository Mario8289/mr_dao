from requests import get


class CyptoWatchBase:
    _KEY = 'A5UICPG17VT0VNB9CIT3'
    _SECRET = 'XkK+7cYvZ0cULT7PS9NSWr2BLKH+9igM6yysX3y'
    _URL = 'https://api.cryptowat.ch'

    def get_optional_parameters(self, **kwargs):
        optional_filters = {k:v for (k, v) in kwargs.items() if v is not None}
        if len(optional_filters) != 0:
            parameters = f"{'&'.join([f'{k}={v}' for (k, v) in optional_filters.items()])}"

        return parameters

    @staticmethod
    def get_json(api_call: str):
        r = get(api_call)
        return r.json()