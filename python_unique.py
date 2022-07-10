from enum import Enum, unique


@unique
class Color(Enum):
    red = 1
    red_alias = 2
#print(Color(1))
#如果要限制定义枚举时，不能定义相同值的成员。可以使用装饰器@unique【要导入unique模块】
# ValueError: duplicate values found in <enum 'Color'>: red_alias -> red
# 再执行就会提示错误
# 确保枚举值唯一
# 我们定义枚举时，成员名称是不可以重复的，但成员值是可以重复的，
# 如果想要保证成员值不可重复，可以通过装饰器 @unique 来实现，如下所示：
@unique
class WeekDay(Enum):
    Mon = 0
    Tue = 1
    Wed = 2
    Thu = 3
# 枚举成员
# print(WeekDay.Mon)
# # 枚举成员名称
# print(WeekDay.Mon.name)
# # 枚举成员值
# print(WeekDay.Mon.value)

# 方式 1
for day in WeekDay:
    # 枚举成员
    print(day)
    # 枚举成员名称
    print(day.name)
    # 枚举成员值
    print(day.value)

# 方式 2
#print(list(WeekDay))