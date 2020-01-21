import requests

class UpdateBooking:
    def __init__(self, config, auth):
        self.url = config.BASE_URL + '/booking'
        self.token = auth.token



def put(self, id, body):
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'token=' + self.token
    }
    res = requests.put(
        url=self.url + id,
        headers=headers,
        data=body
    )
    return res