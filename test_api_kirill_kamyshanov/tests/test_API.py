import requests
import pytest


@pytest.fixture(scope='session')
def session_notifications():
    print("\nStart testing")
    yield
    print("\nTesting completed")


@pytest.fixture(autouse=True, scope='function')
def t_notifications():
    print("\nbefore test")
    yield
    print("\nafter test")


@pytest.fixture()
def setup_and_teardown():
    body = {"name": "Andrey",
            "data": {"feature": "value"}
            }
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body)
    user_id = response.json()['id']
    yield user_id
    requests.delete(f'http://objapi.course.qa-practice.com/object/{user_id}')


body = {"name": "Andrey", "data": {"feature": "value"}}


def test_get_by_id_obj(setup_and_teardown, session_notifications):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{setup_and_teardown}')
    user = response.json()
    print(user)
    assert response.status_code == 200, 'status code is not 200'
    assert user, 'user not found'
    assert "data" in user, 'user does not have data'
    assert "id" in user, 'user does not have id'
    assert "name" in user, 'user does not have name'

#
# # Создание объектов
# @pytest.mark.parametrize("body", [
#     ({"name": "Maria", "data": {"feature": "grape"}}),
#     ({"name": "Anton", "data": {"feature": "desert"}}),
#     ({"name": "Nikita", "data": {"feature": "Астерикс и Обеликс против Цезаря"}})
# ])
# def test_create_obj(body):
#     response = requests.post('http://objapi.course.qa-practice.com/object', json=body)
#     response_body = response.json()
#     print(response_body)
#     assert response.status_code == 200, 'Status code is not 200'
#     assert 'id' in response_body, 'Response body does not have an id'
#     assert 'data' in response_body, 'Response body does not have a data'
#     assert 'name' in response_body, 'Response body does not have a name'
#     assert body['name'] == response.json()['name'], 'name does not match'
#     assert body['data'] == response.json()['data'], 'data does not match'
#
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
