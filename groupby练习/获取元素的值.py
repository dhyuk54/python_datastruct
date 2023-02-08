import pandas as pd
# http://t.zoukankan.com/dataxon-p-12566447.html
df = pd.DataFrame({'Type': ['Apple', 'Pear', 'Orange', 'Grape', 'Banana', 'Lemon', 'Watermelon', 'Tomato'], \
                   'Price': [25, 10, 15, 30, 12, 15, 30, 20]})

print(df)

row_index = df[df.Type == 'Watermelon'].index.tolist()[0]
print(row_index)

Watermelon_price = df['Price'][0]
print(Watermelon_price)
