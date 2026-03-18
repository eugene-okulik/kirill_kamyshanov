import requests
from test_api_kirill_kamyshanov.endpoints.endpoint import Endpoint


class GetObj(Endpoint):

    def get_by_id_obj(self, id):
        self.response = requests.get(f'{self.url}/{id}')
        self.user_id = self.response.json()['id']
        self.status_code = self.response.status_code
        self.response_body = self.response.json()
        print(self.response.json())
        print(self.user_id)
        return self.response