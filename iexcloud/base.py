from requests import get


class IEXBase:

    _TOKENS = {
        "stable": "sk_ff2092d22367451ca4cfed51f0d6cb85",
        "sandbox": "Tsk_3e3a1bbe03f341fd9474990e0e1b857a"
    }

    _URLS = {
        "stable": "https://cloud.iexapis.com",
        "sandbox": "https://sandbox.iexapis.com",
    }

    def __init__(self, sandbox_view=False):
        self.token = self.set_token(sandbox_view)
        self.base_url = self.set_base_url(sandbox_view)
        self.version = "stable"

    def get_query_parameters(self, **kwargs):
        query_parameters: str = ""
        optional_filters = {k:v for (k, v) in kwargs.items() if v is not None}
        if len(optional_filters) != 0:
            query_parameters = f"{'&'.join([f'{k}={v}' for (k, v) in optional_filters.items()])}&"

        return f"?{query_parameters}token={self.token}"

    def get_json(self, api_call: str):
        r = get(api_call)
        return r.json()

    @staticmethod
    def set_token(sandbox_view: bool) -> str:
        if sandbox_view:
            return IEXBase._TOKENS['sandbox']
        else:
            return IEXBase._TOKENS['stable']

    @staticmethod
    def set_base_url(sandbox_view: bool) -> str:
        if sandbox_view:
            return IEXBase._URLS['sandbox']
        else:
            return IEXBase._URLS['stable']
