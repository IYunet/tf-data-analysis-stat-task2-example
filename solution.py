import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2


chat_id = 426527714 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n = x.size
    sum_x_2 = sum([e ** 2 for e in x])
    q_l = chi2(2 * n).ppf(q=alpha / 2)
    q_r = chi2(2 * n).ppf(q=1 - alpha / 2)
    return np.sqrt(sum_x_2 / q_r / 44), np.sqrt(sum_x_2 / q_l / 44)
