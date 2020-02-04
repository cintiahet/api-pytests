import requests


class Bookings:
    def __init__(self, config, auth):
        self.url = config.BASE_URL
        self.token = auth.token

    def get_booking_ids(self):
        res = requests.get(
            url=self.url + '/booking',
        )
        return res

    def get_booking_ids_filter(self, filter):
        res = requests.get(
            url=self.url + '/booking?' + filter,
        )
        return res

    def get_booking(self, id):
        res = requests.get(
            url=self.url + '/booking/' + id,
        )
        return res

    def create_booking(self, body, contenttype):
        res = requests.post(
            url=self.url + '/booking',
            headers={
                'Content-Type': contenttype
            },
            data=body
        )
        return res

    def update_booking(self, id, body, contenttype):
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

    def delete_booking(self, id, contenttype):
        headers = {
            'Content-Type': contenttype,
            'Cookie': 'token=' + self.token
        }
        res = requests.delete(
            url=self.url + '/booking/' + id,
            headers=headers
        )
        return res

    def booking_auth(self, id, body, req_headers, endpoint):

        if endpoint == 'update':
            return requests.put(
                url=self.url + '/booking/' + id,
                headers=req_headers,
                data=body
            )
        elif endpoint == 'delete':
            return requests.delete(
                url=self.url + '/booking/' + id,
                headers=req_headers,
                data=body
            )
        else:
            return 'Method not implemented'
