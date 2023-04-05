import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2


chat_id = 426527714 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    x = x / 44
    n = x.shape[0]
    s2 = ((x - x.mean())**2).mean()
    quant1 = chi2.ppf(1-alpha/2, n-1)
    quant2 = chi2.ppf(alpha/2, n-1)
    left = np.sqrt((n - 1) * s2 / quant1)
    right = np.sqrt((n - 1) * s2 / quant2)
    return (left,right)
