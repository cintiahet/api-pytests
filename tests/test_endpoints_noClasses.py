import requests
import json
import pytest
from .support.assertions import assert_valid_schema


def test_booking_get_all_bookings(config):
    res = requests.get(
        url=config.BASE_URL + '/booking',
        headers={
            'Content-Type': 'application/json'
        }
    )
    assert res.status_code == 200
    assert len(res.json()) > 0
    assert_valid_schema(res.json(), 'bookinglist.json')


def test_booking_get_one(config):
    res = requests.get(
        url=config.BASE_URL + '/booking/3',
        headers={
            'Content-Type': 'application/json'
        }
    )
    assert res.status_code == 200
    assert len(res.json()) > 0
    assert_valid_schema(res.json(), 'booking.json')


def test_booking_get_not_found(config):
    res = requests.get(
        url=config.BASE_URL + '/booking/someWrongApp',
        headers={
            'Content-Type': 'application/json'
        }
    )
    assert res.status_code == 404


def test_booking_post(config, base_data):
    body_data = json.dumps(base_data)
    headers = {
        'Content-Type': 'application/json'
    }
    res = requests.post(
        url=config.BASE_URL + '/booking',
        headers=headers,
        data=body_data
    )

    assert res.status_code == 200
    assert len(res.json()) > 0
    assert_valid_schema(res.json(), 'newbook.json')


@pytest.mark.parametrize("name_cases", [45654, True])
def test_booking_post_name_fail(config, base_data, name_cases):
    data = base_data
    data['firstname'] = name_cases
    body_data = json.dumps(data)
    headers = {
        'Content-Type': 'application/json'
    }
    res = requests.post(
        url=config.BASE_URL + '/booking',
        headers=headers,
        data=body_data
    )
    assert res.status_code == 500
