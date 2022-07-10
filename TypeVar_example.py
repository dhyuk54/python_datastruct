# 自定义泛型
from typing import Generic,TypeVar
# 任意类型
T = TypeVar("T")

def test(name:T)->T:
    print(name)
    return name

print(test(11))
print(test("aa"))


class UserInfo(Generic[T]):
    def __init__(self,v):
        self.v = v

    def get(self):
        return self.v

l = UserInfo("hyuk")
print(l.get())