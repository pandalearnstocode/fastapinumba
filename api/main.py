from fastapi import FastAPI
from pydantic import BaseModel
import core
import numpy as np
class SimulationParameters(BaseModel):
    n: int
    
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/nb_vectorized/")
def nb_vec_api(sim_params: SimulationParameters):
    sum_x = core.softplus_vec_wrap(sim_params.n)
    print(np.ma.masked_invalid(sum_x).sum())
    return sim_params

@app.post("/nb_jit/")
def nb_jit_api(sim_params: SimulationParameters):
    sum_x = core.softplus_vec_wrap(sim_params.n)
    print(np.ma.masked_invalid(sum_x).sum())
    return sim_params

@app.post("/nb_njit/")
def nb_njit_api(sim_params: SimulationParameters):
    sum_x = core.softplus_vec_wrap(sim_params.n)
    print(np.ma.masked_invalid(sum_x).sum())
    return sim_params

@app.post("/nb_njit_fm/")
def nb_njit_fm_api(sim_params: SimulationParameters):
    sum_x = core.softplus_fastmath_njit(sim_params.n)
    print(np.ma.masked_invalid(sum_x).sum())
    return sim_params