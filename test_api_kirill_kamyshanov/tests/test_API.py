import requests
import pytest
# from test_api_kirill_kamyshanov.endpoints.create_obj.CreateObj import create_obj

# class CreateObj:
#     url = 'http://objapi.course.qa-practice.com/object'
#
#     @pytest.fixture
#     def create_object(self, body):
#         response = requests.post(self.url, json=body)
#         user_id = response.json()['id']
#         yield response
#         requests.delete(f'{self.url}/{user_id}')


# @pytest.fixture
# def create_object():
#     body = {"name": "Andrey", "data": {"feature": "value"}}
#     url = 'http://objapi.course.qa-practice.com/object'
#     response = requests.post(url, json=body)
#     user_id = response.json()['id']
#     yield response
#     requests.delete(f'{url}/{user_id}')

# @pytest.fixture(scope='session')
# def session_notifications():
#     print("\nStart testing")
#     yield
#     print("\nTesting completed")
#
#
# @pytest.fixture(autouse=True, scope='function')
# def t_notifications():
#     print("\nbefore test")
#     yield
#     print("\nafter test")


# @pytest.fixture()
# def setup_and_teardown():
#     body = {"name": "Andrey",
#             "data": {"feature": "value"}
#             }
#     response = requests.post('http://objapi.course.qa-practice.com/object', json=body)
#     user_id = response.json()['id']
#     yield user_id
#     requests.delete(f'http://objapi.course.qa-practice.com/object/{user_id}')


body1 = {"name": "Andrey", "data": {"feature": "value"}}

# Чистовик
# def test_get_by_id_obj(create_object_endpoint, get_object_endpoint):
#     user_id = create_object_endpoint.create_test_object(body1)
#     # print(user_id) # отладка
#     resp_body = get_object_endpoint.get_by_id_obj(user_id).json() # пока к json не привожу
#     # print(resp_body) # отладка
#     get_object_endpoint.check_that_status_code_is_200()
#     get_object_endpoint.check_presence_of_response_body(resp_body)
#     get_object_endpoint.check_response_body_fields(resp_body)
#
#     get_object_endpoint.remove_test_object()





# чистовик
# # Создание объектов
# @pytest.mark.parametrize("body", [
#     ({"name": "Maria", "data": {"feature": "grape"}}),
#     ({"name": "Anton", "data": {"feature": "desert"}}),
#     ({"name": "Nikita", "data": {"feature": "Астерикс и Обеликс против Цезаря"}})
# ])
# def test_create_obj(create_object_endpoint, body):
#     response_body = create_object_endpoint.create_object(body).json()
#     print(response_body)
#     create_object_endpoint.check_that_status_code_is_200()
#     create_object_endpoint.check_presence_of_response_body(response_body)
#     create_object_endpoint.check_response_body_fields(response_body)
#     create_object_endpoint.check_name_field(response_body)
#     create_object_endpoint.check_data_field(response_body)
#
#     create_object_endpoint.remove_test_object()














#
# # Изменение объекта с помощью метода PUT
# def test_put_edit_obj(setup_and_teardown):
#     body = {"name": "new_name_put",
#             "data": {"feature": "new_value_put"}
#             }
#     response = requests.put(f'http://objapi.course.qa-practice.com/object/{setup_and_teardown}', json=body)
#     response_body = response.json()
#     print(response_body)
#     assert response.status_code == 200, 'Status code is not 200'
#     assert 'id' in response_body, 'Response body does not have an id'
#     assert 'name' in response_body, 'Response body does not have a name'
#     assert 'data' in response_body, 'Response body does not have a data'
#     assert int(response_body['id']) == setup_and_teardown, 'ID does not match'
#     assert response_body['name'] == body['name'], 'Name does not match'
#     assert response_body['data'] == body['data'], 'Feature does not match'
#
#
# # Изменение объекта с помощью метода PATCH
# @pytest.mark.critical
# def test_patch_edit_obj(setup_and_teardown):
#     body1 = {"name": "new_name_patch"}
#     body2 = {"data": {"feature": "new_value_patch"}}
#
#     response = requests.patch(f'http://objapi.course.qa-practice.com/object/{setup_and_teardown}', json=body1)
#     response_body = response.json()
#     assert response.status_code == 200, 'Status code is not 200'
#     assert 'id' in response_body, 'Response body does not have an id'
#     assert 'data' in response_body, 'Response body does not have a data'
#     assert 'name' in response_body, 'Response body does not have a name'
#     assert response_body['name'] == body1['name'], 'Name does not match'
#
#     response = requests.patch(f'http://objapi.course.qa-practice.com/object/{setup_and_teardown}', json=body2)
#     response_body = response.json()
#     assert response.status_code == 200, 'Status code is not 200'
#     assert response_body['name'] == body1['name'], 'Name does not match'
#     assert response_body['data'] == body2['data'], 'Data does not match'
#
#
# # Удаление объекта
# @pytest.mark.medium
# def test_delete_an_obj(setup_and_teardown):
#     # удаление объекта
#     response = requests.delete(f'http://objapi.course.qa-practice.com/object/{setup_and_teardown}')
#     assert response.status_code == 200, 'Status code is not 200'
#
#     # Проверка того, что объект удалился
#     query = requests.get(f'http://objapi.course.qa-practice.com/object/{setup_and_teardown}')
#     assert query.status_code == 404, 'Status code is not 404'
