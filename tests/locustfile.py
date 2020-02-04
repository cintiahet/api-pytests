from locust import HttpLocust, TaskSet, task, between

class UserBehavior(TaskSet):


    @task(1)
    def bookings(self):
        self.client.get("booking")

    @task(1)
    def bookingsbyID(self):
        self.client.get("booking/3")

    @task(2)
    def create_booking(self):
        payload = { "firstname": "first name n",
                    "lastname": "lastN new",
                    "totalprice": 100,
                    "depositpaid": True,
                    "bookingdates":
                        {"checkin": "2013-02-23", "checkout": "2014-10-23"},
                    "additionalneeds": "blabla"}
        r = self.client.post("booking", json=payload)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5, 9)