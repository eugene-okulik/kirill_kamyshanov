import requests
import allure
from test_api_kirill_kamyshanov.endpoints.endpoint import Endpoint


class GetObj(Endpoint):

    @allure.step('Get a post')
    def get_by_id_obj(self, id):
        self.response = requests.get(f'{self.url}/{id}')
        self.status_code = self.response.status_code
        self.response_body = self.response.json()
        self.user_id = self.response.json()['id']

    # для этого класса переопределил методы проверки полей name и data. Т.к. мы не ждём в них конкретного значения

    @allure.step('Check "name" field')
    def check_name_field(self):
        assert type(self.response_body['name']) is str, 'type "name" is not correct'

    @allure.step('Check "data" field')
    def check_data_field(self):
        assert type(self.response_body['data']) is dict, 'type "data" is not correct'

    # Не стал выносить в род. класс, т.к. метод нужен только для двух эндпойнтов (get patch)

    @allure.step('Check "id" field')
    def check_id_field(self, id):
        assert self.user_id == id, f'ID field does not match {self.user_id} != {id}'
