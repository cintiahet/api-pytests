import pytest
import json
from endpoints.bookings import Bookings
from .support.assertions import assert_valid_schema


@pytest.fixture
def bookings(config, auth):
    return Bookings(config, auth)


@pytest.fixture()
def new_booking(bookings, base_data_fake):
    res = bookings.create_booking(base_data_fake, 'application/json')
    assert res.status_code == 200

    new_booking_id = str(res.json()['bookingid'])

    yield new_booking_id

    res = bookings.delete_booking(new_booking_id, 'application/json')
    assert res.status_code == 201


def test_booking_get_all(bookings):
    res = bookings.get_booking_ids()
    assert res.status_code == 200
    assert len(res.json()) > 0
    assert_valid_schema(res.json(), 'bookinglist.json')


def test_booking_filter_bydate(bookings):
    res = bookings.get_booking_ids_filter('checkin=2013-02-23')
    assert res.status_code == 200
    assert len(res.json()) > 0
    assert_valid_schema(res.json(), 'bookinglist.json')


def test_booking_get_one(bookings, new_booking):
    res = bookings.get_booking(new_booking)
    assert res.status_code == 200
    assert len(res.json()) > 0
    assert_valid_schema(res.json(), 'booking.json')


def test_booking_get_not_found(bookings):
    res = bookings.get_booking("SomeBookingNotExists")
    assert res.status_code == 404


def test_booking_create(bookings, base_data_fake):
    res = bookings.create_booking(base_data_fake, 'application/json')
    assert res.status_code == 200
    assert len(res.json()) > 0
    assert_valid_schema(res.json(), 'newbook.json')


@pytest.mark.parametrize("name_cases", [45654, True, ' '])
def test_booking_create_name_fail(bookings, base_data_fake, name_cases):
    data = json.loads(base_data_fake)
    data['firstname'] = name_cases
    body = json.dumps(data)
    res = bookings.create_booking(body, 'application/json')
    assert res.status_code == 500


def test_booking_update(bookings, auth, new_booking):
    data = (bookings.get_booking(new_booking)).json()
    data['firstname'] = 'updated firstName'
    body = json.dumps(data)
    res = bookings.update_booking(new_booking, body, 'application/json')

    assert res.status_code == 200
    assert len(res.json()) > 0

    resupdate = bookings.get_booking(new_booking)
    assert resupdate.json()['firstname'] == 'updated firstName'
    assert_valid_schema(res.json(), 'booking.json')


def test_booking_delete_e2e(bookings, auth, base_data_fake):
    created_book = bookings.create_booking(base_data_fake, 'application/json')
    created_id = str(created_book.json()['bookingid'])
    if created_book.status_code == 200:
        res_del = bookings.delete_booking(created_id, 'application/json')
        assert res_del.status_code == 201
        res = bookings.get_booking(created_id)
        assert res.status_code == 404

@pytest.mark.parametrize("headers", [{'Content-Type': 'application/json'}, {'Content-Type': 'application/json', 'Cookie': 'token=invalidToken'}])
def test_booking_update_authentication_validation(bookings, new_booking, headers):
    data = json.dumps((bookings.get_booking(new_booking)).json())
    req_headers = headers
    res = bookings.booking_auth(new_booking, data, req_headers, 'update')

    res.status_code == 403

@pytest.mark.parametrize("headers", [{'Content-Type': 'application/json'}, {'Content-Type': 'application/json', 'Cookie': 'token=invalidToken'}])
def test_booking_delete_authentication_validation(bookings, new_booking, headers):
    data = json.dumps((bookings.get_booking(new_booking)).json())
    req_headers = headers
    res = bookings.booking_auth(new_booking, data, req_headers, 'delete')

    res.status_code == 403