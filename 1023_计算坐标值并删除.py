import numpy as np

charter_list = [[133, 18, 25], [33], [31, 24, 23], [12, 18, 42], [49, 16, 35], [], [44, 25]]
charter_width_list = [[142, 18, 27], [33], [31, 24, 32], [12, 18, 34], [49, 16, 22], [], [44, 55]]
filter_charter = [i for i in charter_list if i != []]
filter_charter_width = [i for i in charter_width_list if i != []]
field_width = 60
list3 = []
# print(filter_charter)
# print(filter_charter.index())
# print(filter_charter_width)
# for i in range(len(filter_charter)):
#     new_value = filter_charter[i][-1] + filter_charter_width[i][-1]
#     result = field_width - new_value
#     list3.append(new_value)
#     if result > 10:
#         print("delete row")
for charter, charter_width in zip(filter_charter, filter_charter_width):
    if charter is not None:
        new_value = charter[-1] + charter_width[-1]
        print(new_value)
        result = field_width - new_value
        # 如果 计算后的field的width和文字的width 差过于大的话 那就说明要删除这一行坐标中的数据
        if result > 5:
            print(charter_list.index(charter))
            # 获取要删除的index 通过df.loc[index:index,'column'] = np.nan
            print("pd.loc[charter_list.index(charter),'列'] = np.nan ")
            print("dropna")
