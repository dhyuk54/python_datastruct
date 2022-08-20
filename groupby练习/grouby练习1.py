import pandas as pd
# https://qa.1r1g.com/sf/ask/3207984811/
df = pd.DataFrame({'item_id': ['a', 'a', 'b', 'b', 'b', 'c', 'd'],
                   'cost': [1, 2, 1, 1, 3, 1, 5]})
#print(df)
"""
  item_id  cost
0       a     1
1       a     2
2       b     1
3       b     1
4       b     3
5       c     1
6       d     5
"""
t = df.groupby('item_id').first()  # lost track of the index
print(t)
"""
item_id  cost    
a           1
b           1
c           1
d           5
"""
t = df.groupby('item_id').last()  # lost track of the index
"""
item_id    cost  
a           2
b           3
c           1
d           5
"""
print(t)
desired_row = t[t.cost == t.cost.max()]
print(desired_row)
"""
item_id  cost    
d           5
"""
gb = df.groupby('item_id', as_index=False)
data = gb.groups
print(data)
# {'a': [0, 1], 'b': [2, 3, 4], 'c': [5], 'd': [6]}
subset = {k: max(v) for k, v in data.items()}
print(subset)
# {'a': 1, 'b': 4, 'c': 5, 'd': 6}
df2 = df.loc[subset.values()]
print(df2)
"""
  item_id  cost
1       a     2
4       b     3
5       c     1
6       d     5
"""
result = df[df.index.isin(df2[df2.cost == df2.cost.max()].index)]
print(result)
#   item_id  cost
# 6       d     5
result = df[~df.index.isin(df2[df2.cost == df2.cost.max()].index)]
print(result)
"""
  item_id  cost
0       a     1
1       a     2
2       b     1
3       b     1
4       b     3
5       c     1
"""