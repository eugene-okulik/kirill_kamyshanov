import requests

from test_api_kirill_kamyshanov.endpoints.endpoint import Endpoint

class DeleteObj(Endpoint):
    def delete_an_obj(self, id):
        response = requests.delete(f'{self.url}/{id}')
        print(response.status_code)


    def check_that_status_code_is_404(self):
        self.response = requests.get(f'{self.url}/{id}')
        print(self.response.status_code)
        assert self.response.status_code == 404, 'status code is not 404'