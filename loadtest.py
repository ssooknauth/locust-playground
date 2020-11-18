# A simple loadtest against your local flask server - localhost:9999/test
import time
from locust import HttpUser, task

class TestFlowBasic(HttpUser):
    @task
    def test_path(self):
        self.client.get("/test")
        time.sleep(1)
