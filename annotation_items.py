from typing import Union, List
"""
List[X]: 要素の型がXのリスト（list）
Union[X, Y]: XかYいずれかの型
"""
def func_u(x: List[Union[int, float]]) -> float:
    return sum(x) ** 0.5

print(func_u([0.5, 9.5, 90]))
# 10.0

def func_annotations(x: 'description-x', y: 'description-y') -> 'description-return':
    return x * y

print(type(func_annotations.__annotations__))
# <class 'dict'>

print(func_annotations.__annotations__)
# {'x': 'description-x', 'y': 'description-y', 'return': 'description-return'}

print(func_annotations.__annotations__['x'])
# description-x
