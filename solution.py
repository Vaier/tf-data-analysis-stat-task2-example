import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1251251937

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    loc = x.mean()
    scale = np.std(x, ddof=1) / np.sqrt(len(x))
    t = abs(norm.ppf(alpha / 2))
    lower, upper = loc - t * scale, loc + t * scale
    return lower, upper
