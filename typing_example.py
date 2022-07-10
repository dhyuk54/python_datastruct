"""

Union[int,str] 表示既可以是int,也可以是str
"""

from typing import Union, Optional, List, Dict

vars:Union[int,str]

vars = 1
print(vars)

vars = "123"
print(vars)

# Expected type 'Union[int, str]', got 'list' instead
vars = []
print(vars)

#等价写法
vars:Union[int,str]
#等价于
vars:[int or str]

vars:Union[int]
#等价于
vars:int

#Union[int] == int
# 最终 Union[int] 返回的也是 int 类型
#Union[int,str,int] == Union[int,str]
# 重复的类型参数会自动忽略掉
#Union[int,str] == Union[str,int]
# 自动忽略类型参数顺序
#Union[Union[int,str],float] = Union[int,str,float]
#union 嵌套 union 会自动解包

#Optional 可选类型
def foo_func(arg:Optional[int] = None):
    print(arg)

foo_func()
foo_func(1)


# Optional[] 里面只能写一个数据类型


# 正确
#Optional[str]
#Optional[str, int]
#Optional[Union[str, int, float]]


# 错误
#Optional[List[str]]
#Optional[Dict[str, Any]]

# 别名
vector = List[float]

var: vector = [1.1, 2.2]
# 等价写法
var: List[float] = [1.1, 2.2]




# float 组成的列表别名
vector_list_es = List[float]
# 字典别名
vector_dict = Dict[str, vector_list_es]
# 字典组成列表别名
vector_list = List[vector_dict]

# vector_list 等价写法，不用别名的话，有点像套娃
vector = List[Dict[str, List[float]]]

# 函数
def scale(scalar: float, vector: vector_list) -> vector_list:
    for item in vector:
        for key, value in item.items():
            item[key] = [scalar * num for num in value]
    print(vector)
    return vector


result = scale(2.2, [{"a": [1, 2, 3]}, {"b": [4, 5, 6]}])


# 输出结果
[{'a': [2.2, 4.4, 6.6000000000000005]}, {'b': [8.8, 11.0, 13.200000000000001]}]

print(result)

