import pandas as pd
import numpy as np
df = pd.DataFrame({'DATE': [1, 2, 3, 4, 5], 'VOLUME': [100, 200, 300,400,500], 'PRICE': [214, 234, 253,272,291]})
# 可加工数据往下移动一行,并用0填充空值
#df = df.shift(1,fill_value=0)
# 将前一天的股价作为新的列,
df['PREV_DAY_PIRCE'] = df['PRICE'].shift(1,fill_value = 0)
# 计算出前三天的股价的平均值,并生成出新的列
df['LAST_3_DAYS_AVE_PRICE'] = (df['PRICE'].shift(1,fill_value=0) +
                                 df['PRICE'].shift(1,fill_value=0) +
                                 df['PRICE'].shift(1,fill_value=0)) / 3
# 向前移动数据也是很轻松的，使用-1即可
df['TOMORROW_price'] = df['PRICE'].shift(-1,fill_value=0)
#
print(df)