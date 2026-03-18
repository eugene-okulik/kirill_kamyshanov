import requests

from test_api_kirill_kamyshanov.endpoints.endpoint import Endpoint

class PutObj(Endpoint):
    def put_edit_object(self, body, id):
        response = requests.put(f'http://objapi.course.qa-practice.com/object/{id}', json=body)
        self.status_code = response.status_code
        self.response_body = response.json()
        print(self.user_id)
        print(self.response_body)
        print(self.status_code)
        return response.json()

    # Здесь отдельный метод, т.к. в методе PUT id приходит в строковом формате
    def check_id_field(self):
        assert int(self.response_body['id']) == self.user_id, 'ID does not match'
