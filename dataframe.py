import numpy as np
import pandas as pd


# def header(msg):

df = pd.DataFrame(
    [
    ['jan', 54, 23, 43, 22, 13]
    ['feb', 23, 42, 41, 556, 54]
    ['mar', 45, 52, 51, 96, 43]
    ['apr', 43, 65, 77, 53, 42]
    ],
    index = [0, 1, 2, 3],
    columns = ['month', 'avg high', 'avg low', 'record_high', 'avg']
)
print(df)
