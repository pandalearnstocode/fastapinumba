import numba as nb
import pandas as pd
import numpy as np
from loguru import logger
import numexpr as ne
import sympy
import scipy
logger.info(f"Pandas version: {pd.__version__}")
logger.info(f"Numpy version: {np.__version__}")
logger.info(f"Numba version: {ne.__version__}")
logger.info(f"NumExpr version: {nb.__version__}")
logger.info(f"SymPy version: {sympy.__version__}")
logger.info(f"SciPy version: {scipy.__version__}")