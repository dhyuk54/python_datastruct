
import pandas as pd
import numpy as np

"""
用法说明，官方的用法说明比较简洁：
where ：替换条件（condition）为Flase处的值
mask ：替换条件（condition）为True处的值
where(self, cond, other=nan, inplace=False,
	  axis=None, level=None, errors='' raise', try_cast=False)

mask(self, cond, other=nan, inplace=False,
	  axis=None, level=None, errors='' raise', try_cast=False)

"""

df = pd.DataFrame(np.arange(10).reshape(-1,2),columns=['A','B'])
#print(df)
"""
   A  B
0  0  1
1  2  3
2  4  5
3  6  7
4  8  9
"""
def cond1(x):
    return x % 3 == 0
def mult3(x):
    return x * 3
dfwhere = df.where(cond1,mult3)
#print(dfwhere)

dfmask = df.mask(cond1,mult3)
#print(dfmask)

df1 = pd.DataFrame(np.arange(10).reshape(-1,2),columns=['A','B'])
print(df1)
"""
       A      B
0   True  False
1  False   True
2  False  False
3   True  False
4  False   True
"""
m = df1 % 3 == 0
print(m)
dfwhere = df1.where(m,-df)
print(dfwhere)
"""
   A  B
0  0 -1
1 -2  3
2 -4 -5
3  6 -7
4 -8  9
"""
dfmask = df1.mask(m,-df)
print(dfmask)
"""
   A  B
0  0  1
1  2 -3
2  4  5
3 -6  7
4  8 -9
"""






