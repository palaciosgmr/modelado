import unittest
import pandas as pd
import numpy as np

class MyTestCase(unittest.TestCase):
    def test_something(self):
        s=pd.Series([1, 3, 5, np.nan, 6, 8])

        df=pd.read_csv('../resources/v4test.csv',sep=';',encoding='utf-8',errors='ignore')
        print(df)


def add_numbers(x, y):
    return x + y

add_numbers(1, 2)

