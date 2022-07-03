numbers = {'dozens':[10,20,40],'hundred]':[100,101,120,140]}
#print(numbers['dozens'])
#print(numbers['dozens'][1])

# 70
print(sum(numbers['dozens']))
"""
[10, 20, 40]
20
"""

ppap = {'apple':3,'pen':5}
pets = {'cat':3,'dog':3,'elephant':8}
ld = [ppap,pets]
#print(ld[1])
#print(ld[1]['dog'])

"""
{'cat': 3, 'dog': 3, 'elephant': 8}
3
"""
def reverse_lookup(list1):
    dic1 = {}  # 空の辞書を作成する
    for value in list1:
        dic1[value] = list1.index(value)
        # print(dic1)
    return dic1
reverse_lookup(['apple', 'pen', 'orange'])
"""
apple
{'apple': 0}
pen
{'apple': 0, 'pen': 1}
orange
{'apple': 0, 'pen': 1, 'orange': 2}
"""
##

def handle_collision(dic1, str1):
    if dic1.get(len(str1)) is None:
        ls = [str1]
    else:
        ls = dic1[len(str1)]
        ls.append(str1)
    dic1[len(str1)] = ls
handle_collision({3: ['ham', 'egg'], 6: ['coffee', 'brandy'], 9: ['port wine'], 15: ['curried chicken']}, 'tea')

dic2 = {3: ['ham', 'egg'], 6: ['coffee', 'brandy'], 9: ['port wine'], 15: ['curried chicken']}

str = 'tea'
#print([str]) # ['tea']

a = [[3,5,6],2,3,5]
#print(type(a))
s = 0
for i in a:
    if type(i) is list:
        for j in i:
            if type(j) is int:
                s += j
        print("list_sum",s)
    elif type(i) is int:
        s += i
print("total_sum",s)

"""
list_sum 14
total_sum 24
"""