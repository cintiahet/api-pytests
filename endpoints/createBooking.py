import requests

class CreateBooking:
    def __init__(self, config):
        self.url = config.BASE_URL + '/booking'

    def post(self, body):
        headers = {
            'Content-Type': 'application/json'
        }
        res = requests.post(
            url=self.url,
            headers=headers,
            data=body
        )

        return res