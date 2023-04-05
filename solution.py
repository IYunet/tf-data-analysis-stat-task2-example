import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2


chat_id = 426527714 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:    
    s = 44
    n = x.shape[0]
    alpha = 1 - p    
    scale = np.var(x)
    return np.sqrt(scale / chi2.ppf(1 - alpha / 2, df=n-1) / s), \
           np.sqrt(scale / chi2.ppf(alpha / 2, df=n-1) / s)
