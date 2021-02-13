import numba as nb
import pandas as pd
import numpy as np
from loguru import logger
import numexpr as ne
import sympy
import scipy
from math import * 
logger.info(f"Pandas version: {pd.__version__}")
logger.info(f"Numpy version: {np.__version__}")
logger.info(f"Numba version: {ne.__version__}")
logger.info(f"NumExpr version: {nb.__version__}")
logger.info(f"SymPy version: {sympy.__version__}")
logger.info(f"SciPy version: {scipy.__version__}")

def softplus_np(n):
    x = np.random.uniform(50,150,size = n).astype(np.float32)
    safe = x < 100
    return np.log(1 + np.exp(x * safe)) * safe + x * (1-safe)

def softplus_vec_wrap(n):
    x = np.random.uniform(50,150,size = n).astype(np.float32)
    @nb.vectorize('float32(float32)',target = "parallel")
    def softplus_nb(x):
        safe = (x < 100)
        return np.log(1 + np.exp(x * safe)) * safe + x * (1-safe)
    result = softplus_nb(x)
    return result

softplus_jit = nb.jit(softplus_np)
softplus_njit = nb.njit(softplus_np)
softplus_fastmath_njit = nb.njit(fastmath=True,parallel=True)(softplus_np)
