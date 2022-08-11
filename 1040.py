import re

import pandas as pd

import numpy as np

df = pd.DataFrame({
    'restaurant_id': ['101', 'afasdf', '101', 'ffefaf', '102', 'ffefewq', '107'],
    'address': ['1Andy1', '1Becatou1', '1Ccoityu1', '1Delete1', '1Edny1', '1Family', 'Groupy'],
    'city': ['LonYdon', 'YLondon', 'London', 'Oxford', 'Oxford', 'Durham', 'Durham'],
    'reason_name': ['', '', '', '', '', '', ''],
    '移動株数': ['新+', 'Y', 'Y12+', 'Y1000-', '2000+', '2000-', 'Y-'],
    '2新株': ['10', '500', '48', '12', '21', '22', '14'],
    '新株残高': ['0', '0', '0', '0', '0', '0', '0'],
    '旧残高': ['100', '1000', '1000', '0', '2000', '50', '20'],
    '特殊株残高': ['Y100', '0', '0', '0', '0', '0', '0'],
})
# df['移動株数'] = df['移動株数'].str.findall(r'[-+0-9]+')
# print(df['移動株数'])
# cond1 = df['address'].str.findall(r'[^0-9]+')
# print(cond1)
print(df)
df['reason_name'] = df['restaurant_id'].apply(lambda x: np.nan if x.isdigit() else x)
df['restaurant_id'] = df['restaurant_id'].apply(lambda x: x if x.isdigit() else np.nan)

df['address'] = df['address'].apply(lambda x: re.search(r'[^0-9]+', x).group())
print(df)
cond = df['city'].str.contains('Y')
df['city'] = df['city'].mask(cond, 'Y')


# '移動株数': ['Y1+', 'Y','Y12+','Y1000-','2000+','2000-','Y+'],
# 0 Y100 Y100+ Y100- 1 100+ 100- 可
# Y Y+ Y- 不可
def processing_column_data(element):
    if element == '0' \
            or re.search('[A-Z]', element) \
            and element[1:-1].isdigit() \
            or re.search('[A-Z]', element) \
            and element[1:].isdigit() \
            or element[0].isdigit() \
            or element[0].isdigit() \
            and element.endswith('+') \
            or element[0].isdigit() \
            and element.endswith('-'):
        return element
    return np.nan


df['移動株数'] = df['移動株数'].apply(lambda x: processing_column_data(x))
df['2新株'] = df['2新株'].apply(lambda x: processing_column_data(x))
df['新株残高'] = df['新株残高'].apply(lambda x: processing_column_data(x))
df['旧残高'] = df['旧残高'].apply(lambda x: processing_column_data(x))
df['特殊株残高'] = df['特殊株残高'].apply(lambda x: processing_column_data(x))


def sign_format(element):
    for i in element:
        if str(i).endswith('-'):
            return i[-1] + i[:-1]
        elif str(i).endswith('+'):
            return i[:-1]
        else:
            return i



print("\n")
df['移動株数'] = df['移動株数'].replace({np.nan: 'nan'})
df['移動株数'] = df['移動株数'].str.findall(r'[-+0-9]+')
df['移動株数'] = df['移動株数'].apply(lambda x: sign_format(x))
print(df)
