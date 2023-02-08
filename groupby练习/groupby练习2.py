import pandas as pd
import numpy as np


df = pd.DataFrame({'A': np.random.randint(0, 11, 10 ** 3),
                   'B': np.random.randint(0, 11, 10 ** 3),
                   'C': np.random.randint(0, 11, 10 ** 3),
                   'D': np.random.randint(0, 2, 10 ** 3)})
# print(df)
grouped_by = df.groupby(["A", "B", "C"])
groups = dict(list(grouped_by))
index_dict = {k: v.index.tolist() for k,v in groups.items()}
df["POS"] = df.apply(lambda x: index_dict[(x["A"], x["B"], x["C"])].index(x.name), axis=1)
print(df)