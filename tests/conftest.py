import pytest
import json
import subprocess
from endpoints.auth import Auth
from endpoints.config import Config
from .support.utils import load_file

@pytest.fixture
def config():
    return Config()

@pytest.fixture
def auth(config):
    return Auth(config)

@pytest.fixture
def baseData():

    data = json.loads(load_file('testData.json', 'TestData'))
    return data

