
import pandas as pd
import re


df = pd.DataFrame({'mileage': ['1無名1', '1無名', '無名1'],
                   'engine': ['1.4liter', '1.2liter', '1.5liter'],
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
        # result = re.findall(r'[\D]+', x)
        result = re.findall(r'[^0-9]+', x)
        return result
    except Exception :
        print("三种都没匹配")


df['mileage'] = df['mileage'].apply(keep_behind_digital)
print(df['mileage'])
"""
0    [無名]
1    [無名]
2    [無名]
Name: mileage, dtype: object
"""

