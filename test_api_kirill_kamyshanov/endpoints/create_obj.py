import requests

from test_api_kirill_kamyshanov.endpoints.endpoint import Endpoint


class CreateObj(Endpoint):
    def create_object(self, body):
        self.response = requests.post(self.url, json=body)
        self.response_body = self.response.json()
        self.status_code = self.response.status_code
        self.user_id = self.response_body['id']
        return self.response
