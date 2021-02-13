# Stress testing concurrency of REST APIs using numeric computing stack

## Tools:

* API Layer: FAST API
* Scientific computing: Numpy + Numba
* Stress testing: Locust
* Containerization: Docker compose
* Hosting: Azure container services
* Code profiling: SnakeViz

## Workflow:

* Create some basic python/numpy function
* Create a numba wrapper around it
* Measure performance of each function
* Create a endpoint to call each function
* Create a container hosting all these endpoints
* Create a locust file to call all the endpoints
* Create a container using docker
* Run `api` and `loadtest` container using docker-compose
* Extract api call related statistics
* Compare run-time overhead due to API layer on top of vanilla function call.
* Push docker images to ACR
* Spin-up containers in ACI, measure performance
* Draw a conclusion base of different infra, realistic simulated synthetic load about performance and optimal infra required


## Directory structure



## User guide

### Start FAST API from local
```
uvicorn main:app --reload
```
### Start Locust from local
```
locust --host=http://127.0.0.1:8000
```

## Resources:
* terminalizer: https://github.com/faressoft/terminalizer
* Numba: https://www.youtube.com/watch?v=mDsTkg_IpUk
* Creating snippets in VSC: https://www.youtube.com/watch?v=JIqk9UxgKEc
* Numba Repo: https://github.com/numba/numba-examples/tree/master/notebooks