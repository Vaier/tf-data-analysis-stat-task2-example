import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2

chat_id = 1251251937

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n = len(x)
    x = x**2
    sum = x.sum()
    left = np.sqrt(sum / (24 * chi2.ppf(1 - alpha / 2, n * 2)))
    right = np.sqrt(sum / (24 * chi2.ppf(alpha / 2, n * 2)))
    return left, right
