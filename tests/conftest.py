import pytest
import json
from endpoints.auth import Auth
from endpoints.getAllbooking import GetAllBooking
from endpoints.getOneBooking import GetOneBooking
from endpoints.createBooking import CreateBooking
from endpoints.updateBooking import UpdateBooking
from endpoints.config import Config

@pytest.fixture
def config():
    return Config()

@pytest.fixture
def auth(config):
    return Auth(config)


@pytest.fixture
def getAllBooking(config):
    return GetAllBooking(config)

@pytest.fixture
def getOneBooking(config):
    return GetOneBooking(config)

@pytest.fixture
def updateBooking(config,auth):
    return UpdateBooking(config, auth)

@pytest.fixture
def createBooking(config):
    return CreateBooking(config)

@pytest.fixture
def baseData():
    with open("testData.json") as json_file:
        data = json.load(json_file)
        return data



