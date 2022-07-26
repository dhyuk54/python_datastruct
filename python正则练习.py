
import pandas as pd
import numpy as np



# create a dataframe abut the car price
df = pd.DataFrame({'mileage':['23.4 kmpl','21.4 kmpl','20.4 kmpl'],
                   'engine':['1.4 liter','1.2 liter','1.5 liter'],
                   'power':['80 bhp','90 bhp','95 bhp'],
                   'torque':['114Nm@ 2200~3500rpm','61.1Nm@ 3000rpm','111.7Nm@ 2900~4000rpm']})
df1 = df.copy()
#print(df.head())
"""
     mileage     engine   power                 torque
0  23.4 kmpl  1.4 liter  80 bhp    114Nm@ 2200~3500rpm
1  21.4 kmpl  1.2 liter  90 bhp        61.1Nm@ 3000rpm
2  20.4 kmpl  1.5 liter  95 bhp  111.7Nm@ 2900~4000rpm
"""

df['mileage'] = df['mileage'].apply(lambda x: x.split(' ')[0])
#print(df)
"""
  mileage     engine   power                 torque
0    23.4  1.4 liter  80 bhp    114Nm@ 2200~3500rpm
1    21.4  1.2 liter  90 bhp        61.1Nm@ 3000rpm
2    20.4  1.5 liter  95 bhp  111.7Nm@ 2900~4000rpm
"""
def remove_unit(x):
    result = x.split(' ')
    return result
columns = ['mileage','engine','power']
for column in columns:
    df1[column] = df1[column].apply(remove_unit)
#print(df1)
"""
        mileage        engine      power                 torque
0  [23.4, kmpl]  [1.4, liter]  [80, bhp]    114Nm@ 2200~3500rpm
1  [21.4, kmpl]  [1.2, liter]  [90, bhp]        61.1Nm@ 3000rpm
2  [20.4, kmpl]  [1.5, liter]  [95, bhp]  111.7Nm@ 2900~4000rpm
"""

import re


def keep_behind_digital(x):
    result = re.findall(r'\d+', x)
    return result
df['torque'] = df['torque'].apply(keep_behind_digital)

#print(df.head())
"""
  mileage     engine   power                torque
0    23.4  1.4 liter  80 bhp     [114, 2200, 3500]
1    21.4  1.2 liter  90 bhp         [61, 1, 3000]
2    20.4  1.5 liter  95 bhp  [111, 7, 2900, 4000]
"""

def parse_rpm(torque):
    return max([float(x) for x in re.findall("\d+", torque)])


df1["rpm"] = df1["torque"].map(parse_rpm)

print(df1.head())

"""
        mileage        engine      power                 torque     rpm
0  [23.4, kmpl]  [1.4, liter]  [80, bhp]    114Nm@ 2200~3500rpm  3500.0
1  [21.4, kmpl]  [1.2, liter]  [90, bhp]        61.1Nm@ 3000rpm  3000.0
2  [20.4, kmpl]  [1.5, liter]  [95, bhp]  111.7Nm@ 2900~4000rpm  4000.0
"""

