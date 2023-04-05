import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2


chat_id = 426527714 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = x.shape[0]
    alpha = p
    S2 = np.var(x, ddof=1)
    df = n - 1 # число степеней свободы

    # нахождение квантилей распределения хи-квадрат
    chi2_lower = chi2.ppf(alpha/2, df)
    chi2_upper = chi2.ppf(1 - alpha/2, df)

    # нахождение границ доверительного интервала
    lower_bound = (n-1)*S2/chi2_upper
    upper_bound = (n-1)*S2/chi2_lower
    return np.sqrt(lower_bound), np.sqrt(upper_bound)
