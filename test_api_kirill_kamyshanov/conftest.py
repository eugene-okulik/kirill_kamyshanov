import pytest

from test_api_kirill_kamyshanov.endpoints.create_obj import CreateObj
from test_api_kirill_kamyshanov.endpoints.get_obj import GetObj

@pytest.fixture()
def create_object_endpoint():
    return CreateObj()

@pytest.fixture()
def get_object_endpoint():
    return GetObj()