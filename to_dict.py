import pandas as pd

"""
# 参数
orient ：str {‘dict’, ‘list’, ‘series’, ‘split’, ‘records’, ‘index’}

确定字典值的类型。

1) ‘dict’ (default) : dict 如同 {column -> {index -> value}}

2) ‘list’ : dict 如同  {column -> [values]}

3) ‘series’ : dict 如同  {column -> Series(values)}

4) ‘split’ : dict 如同  {‘index’ -> [index], 

‘columns’ -> [columns],

 ‘data’ -> [values]}

5) ‘records’ : list 如同  [{column -> value}, … , 

{column -> value}]

6) ‘index’ : dict 如同  {index -> {column -> value}}

缩写是允许的。s表示series，sp表示split。

into ：lass, 默认为 dict

collections.abc在返回值中用于所有映射的映射子类。

可以是您想要的映射类型的实际类或空实例。

如果你想要一个collection .defaultdict，你必须初始化它。
"""
"""
#返回值
dict, list 或 collections.abc.Mapping

返回一个collections.abc。表示DataFrame的映射对象。

最终的转换依赖于orient参数。
"""

df = pd.DataFrame({'col1':[1,2],
                   'col2':[0.5,0.75]},
                   index = ['row1','row2'])
print(df)
"""
      col1  col2
row1     1  0.50
row2     2  0.75
"""
print(df.to_dict())
"""
{'col1': {'row1': 1, 'row2': 2}, 'col2': {'row1': 0.5, 'row2': 0.75}}
"""

# 您可以指定返回方向
print(df.to_dict('series'))
"""
{'col1': row1    1
         row2    2
Name: col1, dtype: int64,
'col2': row1    0.50
        row2    0.75
Name: col2, dtype: float64}
"""
print(df.to_dict('split'))
"""
{'index': ['row1', 'row2'], 'columns': ['col1', 'col2'], 'data': [[1, 0.5], [2, 0.75]]}
"""
print(df.to_dict('records'))
"""
[{'col1': 1, 'col2': 0.5}, {'col1': 2, 'col2': 0.75}]
"""
print(df.to_dict('index'))
"""
{'row1': {'col1': 1, 'col2': 0.5}, 'row2': {'col1': 2, 'col2': 0.75}}
"""

#您还可以指定映射类型
from collections import OrderedDict, defaultdict
df.to_dict(into=OrderedDict)
OrderedDict([('col1', OrderedDict([('row1', 1), ('row2', 2)])),
             ('col2', OrderedDict([('row1', 0.5), ('row2', 0.75)]))])
dd = defaultdict(list)
df1 = df.to_dict('records', into=dd)
print(df1)
"""
[defaultdict(<class 'list'>, {'col1': 1, 'col2': 0.5}), 
defaultdict(<class 'list'>, {'col1': 2, 'col2': 0.75})]
"""