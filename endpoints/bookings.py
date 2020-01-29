import requests

class Bookings:
    def __init__(self, config, auth):
        self.url = config.BASE_URL
        self.token = auth.token

    def getbookingids(self):
        res = requests.get(
            url=self.url + '/booking',
            )
        return res

    def getbookingidsfilter(self, filter):
        res = requests.get(
            url=self.url + '/booking?' + filter,
            )
        return res

    def getbooking(self, id):
        res = requests.get(
            url=self.url + '/booking/' + id,
            )
        return res

    def createbooking(self, body, contenttype):
        res = requests.post(
            url=self.url + '/booking',
            headers={
                'Content-Type': contenttype
            },
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

    def deletebooking(self, id, contenttype):
        headers = {
            'Content-Type': contenttype,
            'Cookie': 'token=' + self.token
        }
        res = requests.delete(
            url=self.url + '/booking/' + id,
            headers=headers
        )
        return res