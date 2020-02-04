import pytest
import json
from endpoints.auth import Auth
from endpoints.config import Config
from .support.utils import load_file
from .support.test_data_generator import new_test_client

@pytest.fixture
def config():
    return Config()


@pytest.fixture
def auth(config):
    return Auth(config)


@pytest.fixture
def base_data():
    data = json.loads(load_file('testData.json', 'TestData'))
    return data

@pytest.fixture
def base_data_fake():
    data = json.dumps(new_test_client())
    return data
