import requests
import json
import pytest
from .support.assertions import assert_valid_schema


def test_booking_get_AllBookings(config):
    res = requests.get(
        url=config.BASE_URL + '/booking',
        headers={
            'Content-Type': 'application/json'
        }
    )
    assert res.status_code == 200
    assert len(res.json()) > 0
    assert_valid_schema(res.json(), 'bookinglist.json')

def test_booking_get_One(config):
    res = requests.get(
        url=config.BASE_URL + '/booking/3',
        headers={
            'Content-Type': 'application/json'
        }
    )
    assert res.status_code == 200
    assert len(res.json()) > 0
    assert_valid_schema(res.json(), 'booking.json')

def test_booking_get_NotFound(config):
    res = requests.get(
        url=config.BASE_URL + '/booking/someWrongApp',
        headers={
            'Content-Type': 'application/json'
        }
    )
    assert res.status_code == 404

def test_booking_post(config, baseData):
    bodyData = json.dumps(baseData)
    headers = {
        'Content-Type': 'application/json'
    }
    res = requests.post(
        url=config.BASE_URL + '/booking',
        headers=headers,
        data=bodyData
    )

    assert res.status_code == 200
    assert len(res.json()) > 0
    assert_valid_schema(res.json(), 'newbook.json')

@pytest.mark.parametrize("name_cases", [45654, True])
def test_booking_post_Name_fail(config, baseData, name_cases):
    data = baseData
    data['firstname'] = name_cases
    bodyData = json.dumps(data)
    headers = {
        'Content-Type': 'application/json'
    }
    res = requests.post(
        url=config.BASE_URL + '/booking',
        headers=headers,
        data=bodyData
    )
    assert res.status_code == 500
