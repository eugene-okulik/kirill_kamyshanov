import requests

from test_api_kirill_kamyshanov.endpoints.endpoint import Endpoint

class DeleteObj(Endpoint):
    def delete_an_obj(self):
        requests.delete(f'{self.url}/{self.user_id}')

    def check_that_status_code_is_404(self):
        self.response = requests.get(f'{self.url}/{self.user_id}')
        assert self.response.status_code == 404, 'status code is not 404'