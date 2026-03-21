import requests
import allure

from test_api_kirill_kamyshanov.endpoints.endpoint import Endpoint


class DeleteObj(Endpoint):

    # Переопределил метод для создания объекта, т.к. фикстура с созданием и удалением неприменима
    @allure.step('Create an object')
    def create_test_object(self):
        body = {"name": "Andrey", "data": {"feature": "value"}}
        self.response = requests.post(self.url, json=body)
        self.user_id = self.response.json()['id']

    @allure.step('Delete an object')
    def delete_an_obj(self):
        requests.delete(f'{self.url}/{self.user_id}')

    @allure.step('Check that response code is 404')
    def check_that_object_is_deleted(self):
        self.response = requests.get(f'{self.url}/{self.user_id}')
        assert self.response.status_code == 404, 'status code is not 404'
