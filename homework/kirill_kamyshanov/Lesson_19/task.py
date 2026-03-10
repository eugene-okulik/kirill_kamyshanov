import requests


# Служебная функция для удаления тестовых объектов
def x_clear(object_id):
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')


# Служебная функция для создания тестовых объектов
def x_new_object():
    body = {"name": "Andrey",
            "data": {"feature": "value"}
            }
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body)
    return response.json()['id']


# Создание объекта
def create_obj():
    body = {"name": "stranger",
            "data": {"feature": "value"}
            }
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body)
    object_id = response.json()['id']
    response_body = response.json()  # {'data': {'feature': 'value'}, 'id': 4036, 'name': 'stranger'}
    print(response_body)
    assert response.status_code == 200, 'Status code is not 200'
    assert 'id' in response_body, 'Response body does not have an id'
    assert response_body['name'] == 'stranger', 'Name does not match'
    assert response_body['data'] == {"feature": "value"}, 'Feature does not match'
    x_clear(object_id)


# Изменение объекта с помощью метода PUT
def put_edit_obj():
    object_id = x_new_object()
    body = {"name": "new_name_put",
            "data": {"feature": "new_value_put"}
            }
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{object_id}', json=body)
    # Евгений, привет. Здесь мне показалось странным, что поле 'id' приходит в строковом формате, а не в числовом.
    # В методе x_new_object это поле возвращается как число. Баг для проверки внимательности или особенность?
    response_body = response.json()  # {'data': {'feature': 'new_value_put'}, 'id': '4041', 'name': 'new_name_put'}
    print(response_body)
    assert response.status_code == 200, 'Status code is not 200'
    assert int(response_body['id']) == object_id, 'ID does not match'
    assert response_body['name'] == 'new_name_put', 'Name does not match'
    assert response_body['data'] == {"feature": "new_value_put"}, 'Feature does not match'
    x_clear(object_id)


# Изменение объекта с помощью метода PATCH
def patch_edit_obj():
    object_id = x_new_object()
    body1 = {"name": "new_name_patch"}
    body2 = {"data": {"feature": "new_value_patch"}}
    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{object_id}', json=body1)
    response_body = response.json()

    assert response.status_code == 200, 'Status code is not 200'
    assert response_body['name'] == 'new_name_patch', 'Name does not match'
    assert 'id' in response_body, 'Response body does not have an id'
    assert 'data' in response_body, 'Response body does not have a data'

    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{object_id}', json=body2)
    response_body = response.json()
    assert response.status_code == 200, 'Status code is not 200'
    assert response_body['name'] == 'new_name_patch', 'Name does not match'
    assert response_body['data'] == {"feature": "new_value_patch"}, 'Response body does not have a data'
    assert 'id' in response_body, 'Response body does not have an id'
    x_clear(object_id)


# Удаление объекта
def delete_an_obj():
    object_id = x_new_object()
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')
    assert response.status_code == 200, 'Status code is not 200'

    # Проверка того, что объект удалился
    query = requests.get(f'http://objapi.course.qa-practice.com/object/{object_id}')
    assert query.status_code == 404, 'Status code is not 404'
