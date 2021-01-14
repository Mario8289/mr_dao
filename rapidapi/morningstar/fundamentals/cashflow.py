import requests


class Cashflow:
    #https://morningstar1.p.rapidapi.com/fundamentals/quarterly/cashflow-statement/as-reported?Mic=XLON&Ticker=BOO&rapidapi-key=03ac30376dmsh491ec767ca6b170p1ef1dejsnddad383ab08b
    token = "03ac30376dmsh491ec767ca6b170p1ef1dejsnddad383ab08b"

    headers = {
        'accept': "string",
        'x-rapidapi-key': token,
        'x-rapidapi-host': "morningstar1.p.rapidapi.com"
    }

    def __init__(self):
        self.url = "https://morningstar1.p.rapidapi.com/fundamentals"
        self.dataset = "cashflow-statement"

    def get_cashflow(self, period='yearly', restated=True):
        api_call = f"{self.url}/{period}/{self.dataset}"
        if restated:
            api_call = f"{api_call}/restated"

        query_parameters = {"Mic": "XNAS", "Ticker": "MSFT", "Period": "1"}

        response = requests.request("GET", api_call, headers=Cashflow.headers, params=query_parameters)

        print('done')


if __name__ == "__main__":
    cashflow = Cashflow()
    cashflow.get_cashflow("quarterly")