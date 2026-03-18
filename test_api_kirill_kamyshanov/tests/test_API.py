import pytest


def test_get_by_id_obj(get_object_endpoint, session_notifications):
    body1 = {"name": "Andrey", "data": {"feature": "value"}}
    user_id = get_object_endpoint.create_test_object(body1)
    get_object_endpoint.get_by_id_obj(user_id)
    get_object_endpoint.check_that_status_code_is_200()
    get_object_endpoint.check_presence_of_response_body()
    get_object_endpoint.check_response_body_fields()
    get_object_endpoint.check_name_field(body1)
    get_object_endpoint.check_data_field(body1)

    get_object_endpoint.remove_test_object()


# Создание объектов
@pytest.mark.parametrize("body", [
    ({"name": "Maria", "data": {"feature": "grape"}}),
    ({"name": "Anton", "data": {"feature": "desert"}}),
    ({"name": "Nikita", "data": {"feature": "Астерикс и Обеликс против Цезаря"}})
])
def test_create_obj(create_object_endpoint, body):
    create_object_endpoint.create_object(body)
    create_object_endpoint.check_that_status_code_is_200()
    create_object_endpoint.check_presence_of_response_body()
    create_object_endpoint.check_response_body_fields()
    create_object_endpoint.check_name_field(body)
    create_object_endpoint.check_data_field(body)

    create_object_endpoint.remove_test_object()


# Изменение объекта с помощью метода PUT
def test_put_edit_obj(put_edit_object):
    body1 = {"name": "Andrey", "data": {"feature": "value"}}
    body_put = {"name": "new_name_put", "data": {"feature": "new_value_put"}}
    user_id = put_edit_object.create_test_object(body1)

    put_edit_object.put_edit_object(body_put, user_id)
    put_edit_object.check_that_status_code_is_200()
    put_edit_object.check_presence_of_response_body()
    put_edit_object.check_response_body_fields()
    put_edit_object.check_name_field(body_put)
    put_edit_object.check_data_field(body_put)
    put_edit_object.check_id_field()

    put_edit_object.remove_test_object()


# Изменение объекта с помощью метода PATCH
@pytest.mark.critical
def test_patch_edit_obj(patch_edit_object):
    body = {"name": "Andrey", "data": {"feature": "value"}}
    body1 = {"name": "new_name_patch"}
    body2 = {"data": {"feature": "new_value_patch"}}

    user_id = patch_edit_object.create_test_object(body)

    patch_edit_object.patch_edit_object(body1, user_id)
    patch_edit_object.check_that_status_code_is_200()
    patch_edit_object.check_presence_of_response_body()
    patch_edit_object.check_response_body_fields()
    patch_edit_object.check_name_field(body1)
    patch_edit_object.check_id_field()

    patch_edit_object.patch_edit_object(body2, user_id)
    patch_edit_object.check_that_status_code_is_200()
    patch_edit_object.check_name_field(body1)
    patch_edit_object.check_data_field(body2)

    patch_edit_object.remove_test_object()


# Удаление объекта
@pytest.mark.medium
def test_delete_an_obj(delete_edit_object):
    body = {"name": "Andrey", "data": {"feature": "value"}}
    delete_edit_object.create_test_object(body)

    delete_edit_object.delete_an_obj()
    delete_edit_object.check_that_status_code_is_200()

    # Проверка того, что объект удалился
    delete_edit_object.check_that_object_is_deleted()
