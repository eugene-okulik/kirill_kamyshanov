import requests
import allure
from test_api_kirill_kamyshanov.endpoints.endpoint import Endpoint


class GetObj(Endpoint):

    @allure.step('Get a post')
    def get_by_id_obj(self, id):
        self.response = requests.get(f'{self.url}/{id}')
        self.user_id = self.response.json()['id']
        self.status_code = self.response.status_code
        self.response_body = self.response.json()
        return self.response
