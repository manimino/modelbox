from functools import lru_cache
import joblib


@lru_cache()
def get_model():
    return joblib.load('iris/iris.pkl'), 0
