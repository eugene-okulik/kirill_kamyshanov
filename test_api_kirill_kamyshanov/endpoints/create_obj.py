import requests
import allure

from test_api_kirill_kamyshanov.endpoints.endpoint import Endpoint


class CreateObj(Endpoint):
    @allure.step('Create an object')
    def create_object(self, body):
        self.response = requests.post(self.url, json=body)
        self.response_body = self.response.json()
        self.status_code = self.response.status_code
        self.user_id = self.response_body['id']

    # Переопределил метод для удаления тестовых данных, т.к. фикстура здесь неприменима
    @allure.step('Delete an object')
    def remove_test_object(self):
        print(f'\nУдаление тестового юзера {self.user_id}')
        requests.delete(f'{self.url}/{self.user_id}')
