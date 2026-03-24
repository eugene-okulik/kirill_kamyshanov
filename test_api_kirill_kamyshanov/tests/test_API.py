import pytest


# Получение объекта по ID
def test_get_by_id_obj(get_object_endpoint, setup_and_teardown, session_notifications):
    get_object_endpoint.get_by_id_obj(setup_and_teardown)
    get_object_endpoint.check_that_status_code_is_200()
    get_object_endpoint.check_presence_of_response_body()
    get_object_endpoint.check_response_body_fields()

    get_object_endpoint.check_name_field()
    get_object_endpoint.check_data_field()
    get_object_endpoint.check_id_field(setup_and_teardown)


# Изменение объекта с помощью метода PUT
def test_put_edit_obj(setup_and_teardown, put_edit_object):
    body_put = {"name": "new_name_put", "data": {"feature": "new_value_put"}}

    put_edit_object.put_edit_object(body_put, setup_and_teardown)
    put_edit_object.check_that_status_code_is_200()
    put_edit_object.check_presence_of_response_body()
    put_edit_object.check_response_body_fields()
    put_edit_object.check_name_field(body_put)
    put_edit_object.check_data_field(body_put)
    put_edit_object.check_id_field()


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


# Изменение объекта с помощью метода PATCH
@pytest.mark.critical
def test_patch_edit_obj(setup_and_teardown, patch_edit_object):
    body1 = {"name": "new_name_patch"}
    body2 = {"data": {"feature": "new_value_patch"}}

    patch_edit_object.patch_edit_object(body1, setup_and_teardown)
    patch_edit_object.check_that_status_code_is_200()
    patch_edit_object.check_presence_of_response_body()
    patch_edit_object.check_response_body_fields()
    patch_edit_object.check_name_field(body1)
    patch_edit_object.check_id_field(setup_and_teardown)

    patch_edit_object.patch_edit_object(body2, setup_and_teardown)
    patch_edit_object.check_that_status_code_is_200()
    patch_edit_object.check_name_field(body1)
    patch_edit_object.check_data_field(body2)


# # Удаление объекта
@pytest.mark.medium
def test_delete_an_obj(delete_edit_object):
    delete_edit_object.create_test_object()

    delete_edit_object.delete_an_obj()
    delete_edit_object.check_that_status_code_is_200()

    # Проверка того, что объект удалился
    delete_edit_object.check_that_object_is_deleted()
