import requests
import allure

from test_api_kirill_kamyshanov.endpoints.endpoint import Endpoint


class DeleteObj(Endpoint):
    def delete_an_obj(self):
        requests.delete(f'{self.url}/{self.user_id}')

    @allure.step('Check that response code is 404')
    def check_that_object_is_deleted(self):
        self.response = requests.get(f'{self.url}/{self.user_id}')
        assert self.response.status_code == 404, 'status code is not 404'
