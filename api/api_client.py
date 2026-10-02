import requests

from api.api_config import BASE_URL


class APIClient:

    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.session.headers.update({
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                    })

    def get(self, endpoint):
        return self.session.get(
            f"{self.base_url}{endpoint}",timeout=10
        )

    def post(self, endpoint, payload):
        return self.session.post(
            f"{self.base_url}{endpoint}",
            json=payload,
            timeout=10
        )

    def put(self, endpoint, payload):
        return self.session.put(
        f"{self.base_url}{endpoint}",
        json=payload,
        timeout=10
    )

    def delete(self, endpoint):
        return self.session.delete(f"{self.base_url}{endpoint}",timeout=10)