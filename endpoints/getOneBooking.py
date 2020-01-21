import requests

class GetOneBooking:
    def __init__(self, config):
        self.url = config.BASE_URL + '/booking'

    def get(self, id):
        headers = {
            'Content-Type': 'application/json'
        }
        res = requests.get(
            url=self.url + "/" + id,
            headers=headers)
        return res