import pandas as pd
import re
import numpy as np

# https://note.nkmk.me/python-re-match-search-findall-etc/

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
    except Exception:
        print("三种都没匹配")


def keep_behind_digital_1(x):
    result = re.findall(r'[a-zA-Z][-+0-9]+', x)
    if result == []:
        return np.nan
    return result


# df['mileage'] = df['mileage'].str.extract('([a-zA-Z-+0-9]+)')
# print(df['mileage'] )
# df['mileage'] = df['mileage'].str.startswith('Y')
def formata(x):
    if x.startswith('Y') and (not x.isdigit()) or (x.endswith('+') or x.endswith('-')):
        return np.nan
    return x


# df['mileage'] = df['mileage'].apply(lambda x: x if x.startswith('Y') and x[1].contains('-') and x[1].contains('-') else np.nan)
# df['mileage'] = df['mileage'].apply(lambda x: formata(x))
# df['mileage'] = df['mileage'].astype(str).apply(lambda x: x.extract(('[a-zA-Z-+0-9]+)')))

"""
data = {'mileage': ['Y2000+', 'Y2000-', '2000', '2000+', '2000-', '0']
"""
df = pd.DataFrame({'mileage': ['B2000+', 'Y2000000-', '2000', '2000+', '2000-', 'Y+', 'Y-', '0', np.nan, ''],
                   'engine': ['-1000-', '1000-', '1000+', 'aaaa', 'bbbb', 'ccccc', 'dddd', 'aefa', '', 'basdf'],
                   })
df['mileage'] = df['mileage'].str.extract('([^a-zA-Z-+]+)')
# df['mileage'] = df['mileage'].str.extract('([a-zA-Z-+0-9]+)')
#df['mileage'] = df['mileage'].str.extract('((^[a-zA-Z])|(^[0-9]))([0-9]+)(([0-9]$)|([+-]$))|(^[0-9]$)')

# s = re.compile('((^[a-zA-Z])|(^[0-9]))([0-9]+)(([0-9]$)|([+-]$))|(^[0-9]$)')
# match1 = s.findall('Y-')
# print(match1) #Y
print(df['mileage'])
# df['mileage'] = df['mileage'].astype(str).apply(lambda x: np.nan if re.search('[a-zA-Z]', x) and x[1:].startswith('+')
#                                                                     or x[1:].startswith('-') else x)
# print(df['mileage'])
# print(df['mileage'])
"""
0    Y2000+
1    Y2000-
2      2000
3     2000+
4     2000-
5       NaN
6       NaN
7         0
Name: mileage, dtype: object
"""
