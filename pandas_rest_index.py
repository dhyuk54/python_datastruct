import pandas as pd
"""
reset_index可以还原索引，重新变为默认的整型索引 
DataFrame.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill=”) 
level控制了具体要还原的那个等级的索引 
drop为False则索引列会被还原为普通列，否则会丢失

DataFrame可以通过set_index方法，可以设置单索引和复合索引。 
DataFrame.set_index(keys, drop=True, append=False, inplace=False, verify_integrity=False) 
append添加新索引，drop为False，inplace为True时，索引将会还原为列
"""
df1 = pd.DataFrame([[180,'80','20'],[170,'70','19'],
                   [160,'60','18'], [150, '50','16']],
                columns=['height', 'weight', 'BMI'],
                index=['Sato', 'Tanaka', 'Ito','Yamada'])
print(df1)
"""
        height weight BMI
Sato       180     80  20
Tanaka     170     70  19
Ito        160     60  18
Yamada     150     50  16
"""
df2 = df1.reset_index(drop=True)
print(df2)
"""
   height weight BMI
0     180     80  20
1     170     70  19
2     160     60  18
3     150     50  16
"""

df3 = pd.DataFrame([['John','29','NY'],['Mike','32','NJ'],
                   ['Chloe','35','MA'], ['Emma', '28','WA']],
                columns=['name', 'age', 'state'])
print(df3)
"""
    name age state
0   John  29    NY
1   Mike  32    NJ
2  Chloe  35    MA
3   Emma  28    WA
"""
df4 = df3.set_index(['name'])
print(df4)