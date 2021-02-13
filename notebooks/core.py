import numba as nb
import numpy as np

def softplus_np(n):
    x = np.random.uniform(50,150,size = n).astype(np.float32)
    safe = x < 100
    return np.log(1 + np.exp(x * safe)) * safe + x * (1-safe)

def softplus_vec_wrap(n):
    x = np.random.uniform(50,150,size = n).astype(np.float32)
    @nb.vectorize('float32(float32)',target = "parallel")
    def softplus_nb(x):
        safe = x < 100
        return np.log(1 + np.exp(x * safe)) * safe + x * (1-safe)
    result = softplus_nb(x)
    return result

softplus_jit = nb.jit(softplus_np)
softplus_njit = nb.njit(softplus_np)
softplus_fastmath_njit = nb.njit(fastmath=True,parallel=True)(softplus_np)


params = {"n":2000000}
softplus_np(2000000)
softplus_jit(2000000)
softplus_njit(2000000)
softplus_fastmath_njit(2000000)
softplus_vec_wrap(**params)
