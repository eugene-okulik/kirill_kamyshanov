import requests
import allure
from test_api_kirill_kamyshanov.endpoints.endpoint import Endpoint


class PatchObj(Endpoint):

    def patch_edit_object(self, body, id):
        response = requests.patch(f'{self.url}/{id}', json=body)
        self.status_code = response.status_code
        self.response_body = response.json()

    @allure.step('Check "id" field')
    def check_id_field(self):
        assert self.response_body['id'] == self.user_id, 'ID does not match'
