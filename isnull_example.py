"""
pandas.DataFrame, Seriesにはisnull(), isna()メソッドがある。
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 6))
# Make a few areas have NaN values
df.iloc[1:3, 1] = np.nan
df.iloc[5, 3] = np.nan
df.iloc[7:9, 5] = np.nan
print(df)
"""
          0         1         2         3         4         5
0  0.821557 -0.788582  1.331134  0.359904 -1.416607  0.401412
1 -2.298325       NaN -0.945183  0.880388  0.676035  1.703113
2 -0.265296       NaN  0.198140 -0.579451  0.078530 -1.164169
3  0.963508  0.697855  0.344187  2.548352 -0.276043 -0.294245
4 -0.459239 -1.173832  0.210427 -1.618876  0.458962 -0.696934
5 -0.613510 -1.293590 -2.402726       NaN -0.140293  0.226483
6 -2.216476  0.391887  0.255200  1.318816  0.066784  0.966522
7  0.653197 -0.374548  0.052492  1.825095  1.910621       NaN
8 -0.079391 -1.700494 -0.841146  0.178206  0.025524       NaN
9 -1.948911 -0.362867 -0.518300  0.669537  0.895347  0.750088
"""

print(df.isnull())
print("--------")
print(df.isnull()[5][7]) # 5列 7行数据
print("----------")
"""
       0      1      2      3      4      5
0  False  False  False  False  False  False
1  False   True  False  False  False  False
2  False   True  False  False  False  False
3  False  False  False  False  False  False
4  False  False  False  False  False  False
5  False  False  False   True  False  False
6  False  False  False  False  False  False
7  False  False  False  False  False   True
8  False  False  False  False  False   True
9  False  False  False  False  False  False
"""

print(df.isnull().any())
"""
0    False
1     True
2    False
3     True
4    False
5     True
dtype: bool
"""

print(df[df.isnull().values == True])
"""
          0         1         2         3         4         5
1  0.624967       NaN  0.338320  1.275473 -1.175675  0.560024
2  1.171488       NaN  1.213753 -0.006992  0.635184 -1.323695
5 -0.555854 -1.770010  2.257124       NaN -0.199628  0.398642
7 -0.057323 -0.572428 -1.449002  0.388104 -0.778592       NaN
8  0.534046  1.544068 -0.919924 -0.944687  1.338682       NaN
"""

