
from locust import HttpUser, task, between
from faker import Faker
fake = Faker()

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)  # Seconds between each task (simulates user behavior)

    @task
    def create_shift(self):
        shift_name = fake.job()
        start_time = "09:00"
        end_time = "17:00"

        payload = {
            "shift_name": shift_name,
            "start_time": start_time,
            "end_time": end_time,
            "organization": "xyz"
        }

        with self.client.post("/api/shift/create", json=payload, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed to create shift: {response.text}")