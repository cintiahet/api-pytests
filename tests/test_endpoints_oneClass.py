import pytest
import json
import allure
from endpoints.bookings import Bookings
from .support.assertions import assert_valid_schema

@pytest.fixture
def bookings(config, auth):
    return Bookings(config, auth)

def test_booking_get_all(bookings, auth):
    res = bookings.getbookingids()
    assert res.status_code == 200
    assert len(res.json()) > 0
    assert_valid_schema(res.json(), 'bookinglist.json')

def test_booking_filter_bydate(bookings, auth):
    res = bookings.getbookingidsfilter( 'checkin=2013-02-23')
    assert res.status_code == 200
    assert len(res.json()) > 0
    assert_valid_schema(res.json(), 'bookinglist.json')


def test_booking_get_One(bookings, auth):
    res = bookings.getbooking('3')
    assert res.status_code == 200
    assert len(res.json()) > 0
    assert_valid_schema(res.json(), 'booking.json')


def test_booking_get_NotFound(bookings, auth):
    res = bookings.getbooking("SomeBookingNotExists")
    assert res.status_code == 404


def test_booking_create(bookings, baseData):
    body = json.dumps(baseData)
    res = bookings.createbooking(body, 'application/json')
    assert res.status_code == 200
    assert len(res.json()) > 0
    assert_valid_schema(res.json(), 'newbook.json')

@pytest.mark.parametrize("name_cases", [45654, True])
def test_booking_create_Name_fail(bookings, auth, baseData, name_cases):
    data = baseData
    data['firstname'] = name_cases
    body = json.dumps(data)
    res = bookings.createbooking(body, 'application/json')
    assert res.status_code == 500

def test_booking_update(bookings, auth, baseData):
    data = baseData
    data['firstname'] = 'updated firstName'
    body = json.dumps(data)
    res = bookings.updatebooking('3', body, 'application/json')


    assert res.status_code == 200
    assert len(res.json()) > 0

    resupdate = bookings.getbooking('3')
    assert resupdate.json()['firstname'] == 'updated firstName'
    assert_valid_schema(res.json(), 'booking.json')

def test_booking_delete_e2e(bookings,auth, baseData):
    body = json.dumps(baseData)
    created_book = bookings.createbooking(body, 'application/json')
    created_id = str(created_book.json()['bookingid'])
    if created_book.status_code == 200:
        res_del = bookings.deletebooking(created_id, 'application/json')
        assert res_del.status_code == 201
        res = bookings.getbooking( created_id)
        assert res.status_code == 404

