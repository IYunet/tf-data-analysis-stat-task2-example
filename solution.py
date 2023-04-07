import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2
import scipy.stats as t

chat_id = 426527714 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n = x.shape[0]
    s = ( np.sum((x - x.mean())**2) / (n - 1) )**0.5
    quant1 = chi2.ppf(1-alpha/2, 2*n)
    quant2 = chi2.ppf(alpha/2, 2*n)
    left = np.sqrt(sum(x**2)  / (quant1*44) )
    right = np.sqrt(sum(x**2) / (quant2*44) )
    return (left,right)
