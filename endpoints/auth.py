import requests


class Auth:
    def __init__(self, config):
        self.url = config.BASE_URL + '/auth'
        self.token = self.get_token(config)
        print(self.token)

    def get_token(self, config):
        headers = {
            'Content-Type': 'application/json'
        }
        res = requests.post(
            url=self.url,
            headers=headers,
            json={
                'username': config.USERNAME,
                'password': config.PASSWORD
            }
        )
        print(config.USERNAME, res.json())

        assert res.status_code == 200, 'error message'
        assert 'token' in res.json() and res.json() is not None
        return res.json()['token']
