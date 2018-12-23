import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])

# def header(msg):

df = pd.DataFrame(
    [
    ['jan', 54, 23, 43, 22, 13],
    ['feb', 23, 42, 41, 556, 54],
    ['mar', 45, 52, 51, 96, 43],
    ['apr', 43, 65, 77, 53, 42]
    ],
    index = [0, 1, 2, 3],
    columns = ['month', 'avg high', 'avg low', 'record_high', 'avg', 'hablo']
)

print(s)
print(df)

dates = pd.date_range('20130101', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print (df)


"""
python3 dataframe.py
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
                   A         B         C         D
2013-01-01 -0.355977 -0.029926  0.038396 -0.382847
2013-01-02  0.304073 -1.099698  1.595395 -2.022388
2013-01-03 -0.084207  0.217576  0.712303 -1.099022
2013-01-04  0.094900  0.300104 -0.469745  0.491386
2013-01-05  0.754652 -0.202834  0.044537  0.598363
2013-01-06 -0.460088  0.347080  1.223925 -0.438616"""
