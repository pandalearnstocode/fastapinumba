from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def put_nb_vectorized(self):
        self.client.post("/nb_vectorized", json = {"n": 100000})