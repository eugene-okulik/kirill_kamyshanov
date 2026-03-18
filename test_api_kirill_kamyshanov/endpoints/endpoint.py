import requests


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response_body = None
    user_id = None
    status_code = None

    def create_test_object(self, body):
        self.response = requests.post(self.url, json=body)
        self.user_id = self.response.json()['id']
        self.response_body = self.response.json()
        self.status_code = self.response.status_code
        print(f'\nТестовый юзер: {self.user_id}')
        print(f'Данные тестового юзера: {self.response_body}')
        return self.user_id


    def remove_test_object(self):
        print(f'Удаление тестового юзера {self.user_id}')
        requests.delete(f'{self.url}/{self.user_id}')






    def check_that_status_code_is_200(self):
        assert self.response.status_code == 200, 'status code is not 200'


    def check_response_body_fields(self):
        assert 'id' in self.response_body, 'Response body does not have an id'
        assert 'data' in self.response_body, 'Response body does not have a data'
        assert 'name' in self.response_body, 'Response body does not have a name'

    def check_presence_of_response_body(self):
        assert self.response_body, 'user not found'


    def check_name_field(self, body):
        assert self.response_body['name'] == body['name'], 'Field "name" is incorrect'

    def check_data_field(self, body):
        assert self.response_body['data'] == body['data'], 'Field "data" is incorrect'
