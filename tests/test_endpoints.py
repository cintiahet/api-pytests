import pytest
import json
from endpoints.getAllbooking import GetAllBooking
from endpoints.getOneBooking import GetOneBooking
from endpoints.createBooking import CreateBooking
from endpoints.updateBooking import UpdateBooking
from .support.assertions import assert_valid_schema

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

def test_booking_get_all(getAllBooking):
    res = getAllBooking.get()
    assert res.status_code == 200
    assert len(res.json()) > 0
    assert_valid_schema(res.json(), 'bookinglist.json')

def test_booking_get_One(getOneBooking):
    res = getOneBooking.get("3")
    assert res.status_code == 200
    assert len(res.json()) > 0
    assert_valid_schema(res.json(), 'booking.json')

def test_booking_get_NotFound(getOneBooking):
    res = getOneBooking.get("SomeBookingNotExists")
    assert res.status_code == 404

def test_booking_post(createBooking, baseData):
    body = json.dumps(baseData)
    res = createBooking.post(body)
    assert res.status_code == 200
    assert len(res.json()) > 0
    assert_valid_schema(res.json(), 'newbook.json')

@pytest.mark.parametrize("name_cases", [45654, True])
def test_booking_post_Name_fail(createBooking, baseData, name_cases):
    data = baseData
    data['firstname'] = name_cases
    body = json.dumps(data)
    res = createBooking.post(body)
    assert res.status_code == 500


