import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response_body = None
    user_id = None
    status_code = None

    @allure.step('Check that response is 200')
    def check_that_status_code_is_200(self):
        assert self.response.status_code == 200, 'status code is not 200'

    @allure.step('Check that response is have all fields')
    def check_response_body_fields(self):
        assert 'id' in self.response_body, 'Response body does not have an id'
        assert 'data' in self.response_body, 'Response body does not have a data'
        assert 'name' in self.response_body, 'Response body does not have a name'

    @allure.step('Check that response is exist')
    def check_presence_of_response_body(self):
        assert self.response_body, 'user not found'

    @allure.step('Check "name" field')
    def check_name_field(self, body):
        assert self.response_body['name'] == body['name'], 'Field "name" is incorrect'

    @allure.step('Check "data" field')
    def check_data_field(self, body):
        assert self.response_body['data'] == body['data'], 'Field "data" is incorrect'
