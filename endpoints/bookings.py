import requests

class Bookings:
    def __init__(self, config, auth):
        self.url = config.BASE_URL
        self.token = auth.token

    def getbookingids(self, headers):
        res = requests.get(
            url=self.url + '/booking',
            headers=headers)
        return res

    def getbooking(self, headers, id):
        res = requests.get(
            url=self.url + '/booking/' + id,
            headers=headers)
        return res

    def createbooking(self, body, headers):
        res = requests.post(
            url=self.url + '/booking',
            headers=headers,
            data=body
        )
        return res

    def updatebooking(self, id, body, contenttype):
        headers = {
            'Content-Type': contenttype,
            'Cookie': 'token=' + self.token
        }
        res = requests.put(
            url=self.url + '/booking/' + id,
            headers=headers,
            data=body
        )
        return res