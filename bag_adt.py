

class Bag(object):

    def __init__(self,maxsize = 10):
        self.maxsize = maxsize
        self._items = list()

    def add(self,item):
        if len(self) > self.maxsize:
            raise Exception("Bag is Full")
        self._items.append(item)

    def remove(self,item):
        self._items.remove(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item

def test_bag():
    bag = Bag()
    bag.add(1)
    bag.add(2)
    bag.add(3)

    assert len(bag) == 3
    print("assert execute_1")
    bag.remove(3)

    assert len(bag) == 2
    print("assert execute_2")
    for i in bag:
        print(i)


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 使用 yield
        # print b
        a, b = b, a + b
        n = n + 1


for n in fab(5):
    print(n)