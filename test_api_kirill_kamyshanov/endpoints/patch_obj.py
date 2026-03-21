import requests
import allure
from test_api_kirill_kamyshanov.endpoints.endpoint import Endpoint


class PatchObj(Endpoint):

    @allure.step('Edit an object with PATCH')
    def patch_edit_object(self, body, id):
        self.response = requests.patch(f'{self.url}/{id}', json=body)
        self.status_code = self.response.status_code
        self.response_body = self.response.json()
        self.user_id = self.response_body['id']

    # Не стал выносить в род. класс, т.к. метод нужен только для двух эндпойнтов (get patch)
    @allure.step('Check "id" field')
    def check_id_field(self, id):
        assert self.user_id == id, f'ID field does not match: {self.user_id} != {id}'
