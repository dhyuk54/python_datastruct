import numpy as np
import pandas as pd

#method = ‘ffill’ : 是用每一列/行前面的值填充后面的空白
#method = ‘bfill’: 是用每一列/行后面的值填充前面的空白
#
df = pd.DataFrame([
                    [np.nan,2,np.nan,0],
                   [3,4,np.nan,1],
                   [np.nan,np.nan,np.nan,5],
                   [np.nan,3,np.nan,4]],
                  columns=list("ABCD"))
print(df)
"""
     A    B   C  D
0  NaN  2.0 NaN  0
1  3.0  4.0 NaN  1
2  NaN  NaN NaN  5
3  NaN  3.0 NaN  4

"""
# 用 0 替换所有 NaN 元素。
print(df.fillna(0))
"""
     A    B    C  D
0  0.0  2.0  0.0  0
1  3.0  4.0  0.0  1
2  0.0  0.0  0.0  5
3  0.0  3.0  0.0  4
"""
# 我们还可以向前或向后传播非空值。
"""
0  NaN  2.0 NaN  0
1  3.0  4.0 NaN  1
2  3.0  4.0 NaN  5
3  3.0  3.0 NaN  4
"""
print(df.fillna(method="ffill"))
"""
     A    B    C  D
0  0.0  2.0  2.0  0
1  3.0  4.0  2.0  1
2  0.0  1.0  2.0  5
3  0.0  3.0  2.0  4
"""
# 3、将“A”、“B”、“C”和“D”列中的所有 NaN 元素分别替换为 0、1、2 和 3。
values = {"A":0,"B":1,"C":2,"D":3}
print(df.fillna(value = values))
"""
     A    B    C  D
0  0.0  2.0  2.0  0
1  3.0  4.0  2.0  1
2  0.0  1.0  2.0  5
3  0.0  3.0  2.0  4
"""

# 4、只替换第一个 NaN 元素。
print(df.fillna(value=values, limit=1))
"""
     A    B    C  D
0  0.0  2.0  2.0  0
1  3.0  4.0  NaN  1
2  NaN  1.0  NaN  5
3  NaN  3.0  NaN  4
"""
# 5、使用 DataFrame 填充时，替换沿相同的列名和相同的索引发生
df2 = pd.DataFrame(np.zeros((4,4)),columns=list("ABCD"))
print(df.fillna(df2))
"""
     A    B    C  D
0  0.0  2.0  0.0  0
1  3.0  4.0  0.0  1
2  0.0  0.0  0.0  5
3  0.0  3.0  0.0  4
"""








