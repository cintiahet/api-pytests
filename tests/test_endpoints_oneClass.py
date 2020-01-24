import pytest
import json
from endpoints.bookings import Bookings
from .support.assertions import assert_valid_schema

@pytest.fixture
def bookings(config, auth):
    return Bookings(config, auth)

def test_booking_get_all(bookings, auth):
    res = bookings.getbookingids({'Content-Type': 'application/json'})
    assert res.status_code == 200
    assert len(res.json()) > 0
    assert_valid_schema(res.json(), 'bookinglist.json')


def test_booking_get_One(bookings, auth):
    res = bookings.getbooking({'Content-Type': 'application/json'}, '3')
    assert res.status_code == 200
    assert len(res.json()) > 0
    assert_valid_schema(res.json(), 'booking.json')


def test_booking_get_NotFound(bookings, auth):
    res = bookings.getbooking({'Content-Type': 'application/json'}, "SomeBookingNotExists")
    assert res.status_code == 404


def test_booking_create(bookings, baseData):
    body = json.dumps(baseData)
    res = bookings.createbooking(body, {'Content-Type': 'application/json'})
    assert res.status_code == 200
    assert len(res.json()) > 0
    assert_valid_schema(res.json(), 'newbook.json')

@pytest.mark.parametrize("name_cases", [45654, True])
def test_booking_create_Name_fail(bookings, auth, baseData, name_cases):
    data = baseData
    data['firstname'] = name_cases
    body = json.dumps(data)
    res = bookings.createbooking(body, {'Content-Type': 'application/json'})
    assert res.status_code == 500

def test_booking_update(bookings, auth, baseData):
    data = baseData
    data['firstname'] = 'updated firstName'
    body = json.dumps(data)
    res = bookings.updatebooking('3', body, 'application/json')
    assert res.status_code == 200
    assert len(res.json()) > 0

    resupdate = bookings.getbooking({'Content-Type': 'application/json'}, '3').json()
    assert resupdate['firstname'] == 'updated firstName'
    assert_valid_schema(res.json(), 'booking.json')