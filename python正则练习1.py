
import pandas as pd
import re
import numpy as np


df = pd.DataFrame({'mileage': ['1無名1', '1無名', '無名1', '無名1', '無名1', '無名1'],
                   'engine': ['-1000-', '1000-', '1000+', 'aaaa', 'bbbb', 'ccccc'],
                   })
# print(df)
"""
  mileage     engine
0    1無名1  1.4 liter
1    1無名1  1.2 liter
2    k無名1  1.5 liter
"""

def keep_behind_digital(x):
    try:
        #result = re.findall(r'[\D]+', x)
        result = re.findall(r'[^0-9]+', x)

        return result
    except Exception :
        print("三种都没匹配")


def keep_behind_digital_1(x):
        result = re.findall(r'[-+0-9]+', x)
        if result == []:
            return np.nan
        return result


df['mileage'] = df['mileage'].apply(keep_behind_digital)
df['engine'] = df['engine'].apply(keep_behind_digital_1)
print(df['mileage'])
"""
0    [無名]
1    [無名]
2    [無名]
3    [無名]
4    [無名]
5    [無名]
Name: mileage, dtype: object
"""
print(df['engine'])
"""
0    [-1000-]
1     [1000-]
2     [1000+]
3         NaN
4         NaN
5         NaN
Name: engine, dtype: object
"""

