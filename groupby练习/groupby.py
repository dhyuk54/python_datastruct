import pandas as pd
# https://www.yutaka-note.com/entry/pandas_groupby
my_index = ["A", "B", "C", "A", "B", "A"]
my_data = {"Data1": [1, 2, 3, 3, 2, 1], "Data2": [50, 40, 30, 20, 10, 0]}
df = pd.DataFrame(my_data, index=pd.Index(my_index, name="Team"))
print(df)
# サンプルDataFrameの用意
my_index = ["A", "B", "C", "A", "B", "A"]
my_data = {"Data1": [1, 2, 3, 3, 2, 1], "Data2": [50, 40, 30, 20, 10, 0]}

df = pd.DataFrame(my_data, index=pd.Index(my_index, name="Team"))

print(df)
#       Data1  Data2
# Team
# A         1     50
# B         2     40
# C         3     30
# A         3     20
# B         2     10
# A         1      0

# groupbyによる集計例（グループごとに合計値計算）
df_grouped = df.groupby("Team").sum()
print(df_grouped)
#       Data1  Data2
# Team
# A         5     70
# B         4     50
# C         3     30

my_data = {"Team": ["A", "B", "C", "A", "B", "A"],
           "Data1": [1, 2, 3, 3, 2, 1],
           "Data2": [50, 40, 30, 20, 10, 0]}

df = pd.DataFrame(my_data)
#       Data1  Data2
# Team
# A         1     50
# B         2     40
# C         3     30
# A         3     20
# B         2     10
# A         1      0
# グループ分け結果一覧
df.groupby("Team").groups
# {'A': Int64Index([0, 3, 5], dtype='int64'),
#  'B': Int64Index([1, 4], dtype='int64'),
#  'C': Int64Index([2], dtype='int64')}

# グループ名一覧
list(df.groupby("Team").groups.keys())
# ['A', 'B', 'C']

[*df.groupby("Team").groups]
# ['A', 'B', 'C']

# グループ数
len(df.groupby("Team").groups)
# 3

# グループ内要素の個数
df.groupby("Team").size()
# Team
# A    3
# B    2
# C    1
# dtype: int64

# グループ内要素の種類の数（重複なしカウント）
df.groupby("Team").nunique()
#       Team  Data1  Data2
# Team
# A        1      2      3
# B        1      1      2
# C        1      1      1

df_a = df.groupby("Team").get_group("A")
print(df_a)
#   Team  Data1  Data2
# 0    A      1     50
# 3    A      3     20
# 5    A      1      0

df_b = df.groupby("Team").get_group("B")
print(df_b)
#   Team  Data1  Data2
# 1    B      2     40
# 4    B      2     10

df_c = df.groupby("Team").get_group("C")
print(df_c)
#   Team  Data1  Data2
# 2    C      3     30
df.groupby("Team").apply(print)
#   Team  Data1  Data2
# 0    A      1     50
# 3    A      3     20
# 5    A      1      0
#   Team  Data1  Data2
# 1    B      2     40
# 4    B      2     10
#   Team  Data1  Data2
# 2    C      3     30

# .apply(a: a[:])の例
df_visualized = df.groupby("Team").apply(lambda a: a[:])
print(df_visualized)
#        Team  Data1  Data2
# Team
# A    0    A      1     50
#      3    A      3     20
#      5    A      1      0
# B    1    B      2     40
#      4    B      2     10
# C    2    C      3     30

my_data = {"Team": ["A", "B", "C", "A", "B", "A"],
           "Genre": ["alpha", "alpha", "alpha", "beta", "beta", "beta"],
           "Data1": [1, 2, 3, 3, 2, 1], "Data2": [50, 40, 30, 20, 10, 0]}

df = pd.DataFrame(my_data)

print(df)
#   Team  Genre  Data1  Data2
# 0    A  alpha      1     50
# 1    B  alpha      2     40
# 2    C  alpha      3     30
# 3    A   beta      3     20
# 4    B   beta      2     10
# 5    A   beta      1      0
df_visualized = df.groupby("Team").apply(lambda a: a[:])
print(df_visualized)
#        Team  Genre  Data1  Data2
# Team
# A    0    A  alpha      1     50
#      3    A   beta      3     20
#      5    A   beta      1      0
# B    1    B  alpha      2     40
#      4    B   beta      2     10
# C    2    C  alpha      3     30

df_visualized = df.groupby("Genre").apply(lambda a: a[:])
print(df_visualized)
#         Team  Genre  Data1  Data2
# Genre
# alpha 0    A  alpha      1     50
#       1    B  alpha      2     40
#       2    C  alpha      3     30
# beta  3    A   beta      3     20
#       4    B   beta      2     10
#       5    A   beta      1      0

df.groupby("Genre").sum()
#        Data1  Data2
# Genre
# alpha      6    120
# beta       6     30

df_visualized = df.groupby(["Team", "Genre"]).apply(lambda a:a[:])
print(df_visualized)
#              Team  Genre  Data1  Data2
# Team Genre
# A    alpha 0    A  alpha      1     50
#      beta  3    A   beta      3     20 #Aのbetaグループに注目
#            5    A   beta      1      0 #Aのbetaグループに注目
# B    alpha 1    B  alpha      2     40
#      beta  4    B   beta      2     10
# C    alpha 2    C  alpha      3     30