import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 516575251

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    chi2_val = chi2.ppf(1-alpha/2, df = len(x)-1)
    left_bound = np.sqrt((len(x)*np.var(x))/chi2_val)
    right_bound = np.sqrt((len(x)*np.var(x))/chi2.ppf(alpha/2, df=len(x)-1))
    return left_bound, right_bound
