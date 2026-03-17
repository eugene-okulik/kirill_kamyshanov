import requests

class CreateObj:
    url = 'http://objapi.course.qa-practice.com/object'

    def create_object(self, body):
        response = requests.post(self.url, json=body)
        user_id = response.json()['id']
        yield response
        requests.delete(f'{self.url}/{user_id}')


