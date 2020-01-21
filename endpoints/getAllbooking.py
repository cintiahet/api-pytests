import requests

class GetAllBooking:
    def __init__(self, config):
        self.url = config.BASE_URL + '/booking'

    def get(self):
        headers = {
            'Content-Type': 'application/json'
        }
        res = requests.get(
            url=self.url,
            headers=headers)
        return res
