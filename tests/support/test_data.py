from random import randint
from faker import Faker

def new_test_client():
    fake = Faker()
    client_data = {}
    client_data['firstname'] =fake.first_name()
    client_data['lastname'] = fake.last_name()
    client_data['totalprice'] =  randint(300, 5000)
    client_data['depositpaid'] = fake.boolean()
    checkin = (fake.date_between(start_date='+5d', end_date='+6d')).strftime('%Y-%m-%d')
    checkout = fake.date_between(start_date='+10d', end_date='+12d').strftime('%Y-%m-%d')
    client_data['bookingdates'] = {'checkin': checkin, 'checkout': checkout}
    client_data['additionalneeds'] = fake.sentence()

    return client_data




