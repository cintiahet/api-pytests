import pytest
import json
from endpoints.auth import Auth
from endpoints.config import Config

@pytest.fixture
def config():
    return Config()

@pytest.fixture
def auth(config):
    return Auth(config)

@pytest.fixture
def baseData():
    with open("testData.json") as json_file:
        data = json.load(json_file)
        return data



