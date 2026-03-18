import pytest

from test_api_kirill_kamyshanov.endpoints.create_obj import CreateObj
from test_api_kirill_kamyshanov.endpoints.delete_obj import DeleteObj
from test_api_kirill_kamyshanov.endpoints.get_obj import GetObj
from test_api_kirill_kamyshanov.endpoints.put_obj import PutObj
from test_api_kirill_kamyshanov.endpoints.patch_obj import PatchObj

@pytest.fixture()
def create_object_endpoint():
    return CreateObj()

@pytest.fixture()
def get_object_endpoint():
    return GetObj()

@pytest.fixture()
def put_edit_object():
    return PutObj()

@pytest.fixture()
def patch_edit_object():
    return PatchObj()

@pytest.fixture()
def delete_edit_object():
    return DeleteObj()