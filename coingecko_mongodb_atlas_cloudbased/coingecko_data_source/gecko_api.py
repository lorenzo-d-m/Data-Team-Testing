import requests

class Gecko_API:
    def __init__(self):
        self.base_url = 'https://api.coingecko.com/api/v3/'

    def simple_price(self, ids, vs_currencies):
        return requests.get(
            self.base_url + \
            f'simple/price?ids={ids}&vs_currencies={vs_currencies}&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true&precision=full'
            ).json()
