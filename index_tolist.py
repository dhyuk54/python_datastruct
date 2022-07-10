# 范例1：采用Index.tolist()
# 函数将索引转换为列表。

# importing pandas as pd
import pandas as pd

# Creating the index
idx = pd.Index(['Harry', 'Mike', 'Arther', 'Nick'],
               name='Student')

# Print the Index
print(idx)
"""
Index(['Harry', 'Mike', 'Arther', 'Nick'], dtype='object', name='Student')
"""

# 让我们将索引转换为列表。 convert the index into a list
index_list = idx.tolist()
print(index_list)
# ['Harry', 'Mike', 'Arther', 'Nick']

# 范例2：采用Index.tolist()函数将索引转换为python列表。
# Creating the index
idx1 = pd.Index(['2000-01-02', '2000-02-05', '2000-05-11',
                '2001-02-11', '2005-11-12'])

# Print the Index
#print(idx1)
# Index(['2000-01-02', '2000-02-05', '2000-05-11', '2001-02-11', '2005-11-12'], dtype='object')
# convert the index into a list
index1 = idx1.tolist()
print(index1)
"""
['2000-01-02', '2000-02-05', '2000-05-11', '2001-02-11', '2005-11-12']
"""