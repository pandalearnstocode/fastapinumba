from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task(10)
    def put_nb_vectorized(self):
        self.client.post("/nb_vectorized", json = {"n": 10000})
    @task(10)
    def put_nb_jit(self):
        self.client.post("/nb_jit", json = {"n": 10000})
    @task(10)
    def put_nb_njit(self):
        self.client.post("/nb_njit", json = {"n": 10000})
    @task(10)
    def put_nb_njit_fm(self):
        self.client.post("/nb_njit_fm", json = {"n": 10000})