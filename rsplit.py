# 使用后跟空格的逗号作为分隔符，将字符串拆分为列表：
txt = "apple, banana, cherry"

x = txt.rsplit(",")

print(x)
"""
['apple', ' banana', ' cherry']
"""

txt = "apple, banana, cherry"

# 将 max 参数设置为 1，将返回包含 2 个元素的列表！
x = txt.rsplit(", ", 1)

print(x)
"""
['apple, banana', 'cherry']
"""