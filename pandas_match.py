import numpy as np
import pandas as pd

import re
s = pd.Series(['Lion', 'Monkey', 'Rabbit'])
s.str.findall('Monkey')
print(s)
'''
0          []
1    [Monkey]
2          []
dtype: object
'''

# 大小写敏感，不会查出内容
s.str.findall('MONKEY')
# 忽略大小写
import re
s.str.findall('MONKEY', flags=re.IGNORECASE)
# 包含 on
print(s.str.findall('on'))
"""
0    [on]
1    [on]
2      []
"""
# 以 on 结尾
print(s.str.findall('on$'))
""""
dtype: object
0    [on]
1      []
2      []
"""
# 包含多个的会形成一个列表
print(s.str.findall('b'))
"""
dtype: object
0        []
1        []
2    [b, b]
"""
s1 = pd.Series(['Mouse', 'dog', 'house and parrot', '23', np.NaN])
s1.str.contains('og', regex=False)
'''
0    False
1     True
2    False
3    False
4      NaN
dtype: object
'''



# 确定每个字符串是否与正则表达式匹配。
# 第一部分匹配数组0-9，第二位匹配字符a-z
df = pd.Series(['1', '2', '3a', '3b', '03c'],
          dtype="string").str.match(r'[0-9][a-z]')
'''
0    False
1    False
2     True
3     True
4    False
dtype: boolean
'''
print(df)
"""
.str.extract 可以利用正则将文本中的数据提取出来形成单独的列，
下列中正则将文本分为两部分，
第一部分匹配 ab 三个字母，
第二位匹配数字，最终得这两列，
c3 由于无法匹配，最终得到两列空值。
"""
# print((pd.Series(['a1', 'b2', 'c3'],
#           dtype="string")
#  .str
#  .extract(r'([ab])(\d)', expand=True)
# ))
"""
      0     1
0     a     1
1     b     2
2  <NA>  <NA>
"""
s = pd.Series(['a1', 'b2', 'c3'])
print(s.str.extract(r'([ab])?(\d)'))
"""
     0  1
0    a  1
1    b  2
2  NaN  3
"""
# 取正则组的命名为列名
print(s.str.extract(r'(?P<letter>[ab])(?P<digit>\d)'))
'''
  letter digit
0      a     1
1      b     2
2    NaN   NaN
'''
# 匹配全部，会将一个文本中所有符合规则的匹配出来，最终形成一个多层索引数据：
s = pd.Series(["a1a2", "b1b7", "c1"],
              index=["A", "B", "C"],
              dtype="string")
two_groups = '(?P<letter>[a-z])(?P<digit>[0-9])'
s.str.extract(two_groups, expand=True) # 单次匹配
print(s.str.extractall(two_groups))
"""
        letter digit
  match             
A 0          a     1
  1          a     2
B 0          b     1
  1          b     7
C 0          c     1
"""