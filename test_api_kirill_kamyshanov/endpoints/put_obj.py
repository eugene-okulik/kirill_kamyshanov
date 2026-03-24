import requests
import allure
from test_api_kirill_kamyshanov.endpoints.endpoint import Endpoint


class PutObj(Endpoint):
    @allure.step('Edit an object with PUT')
    def put_edit_object(self, body, id):
        self.response = requests.put(f'{self.url}/{id}', json=body)
        self.status_code = self.response.status_code
        self.response_body = self.response.json()
        self.user_id = self.response_body['id']

    # Здесь отдельный метод, т.к. в методе PUT id приходит в строковом формате
    @allure.step('Check "id" field')
    def check_id_field(self):
        assert type(int(self.user_id)) == int, 'type ID is not correct'
