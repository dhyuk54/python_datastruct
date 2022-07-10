from typing import Callable
"""
是一个可调用对象类型
查看对象是否可调用
"""
# # 返回True或False
# isinstance(对象, Callable)


# 最简单的函数
def print_name(name: str):
    print(name)


# 判断函数是否可调用
print(isinstance(print_name, Callable))

x = 1
print(isinstance(x, Callable))

# 函数是可调用的，所以是 True，而变量不是可调用对象，所以是 False

# 输出结果
True
False


def print_name(name: str):
    print(name)


# Callable 作为函数参数使用，其实只是做一个类型检查的作用，检查传入的参数值 get_func 是否为可调用对象
def get_name(get_func: Callable[[str], None]):
    return get_func


vars = get_name(print_name)
vars("test")


# 等价写法，其实就是将函数作为参数传入
def get_name_test(func):
    return func


vars2 = get_name_test(print_name)
vars2("小菠萝")


# 输出结果
#test
#小菠萝

# Callable  作为函数返回值使用，其实只是做一个类型检查的作用，看看返回值是否为可调用对象
def get_name_return() -> Callable[[str], None]:
    return print_name


vars = get_name_return()
vars("test")


# 等价写法，相当于直接返回一个函数对象
def get_name_test():
    return print_name


vars2 = get_name_test()
vars2("小菠萝")


# 输出结果
#test
#小菠萝