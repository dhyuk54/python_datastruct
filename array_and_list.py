from array import array    # python 提供的比较原始的 array 类


arr = array('u', 'asdf')

#print(arr[0], arr[1], arr[2], arr[3])


# 实现定长的 Array ADT，省略了边界检查等

class Array(object):

    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size
        print(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


def test_array():
    size = 10
    a = Array(size)
    print(a)
    a[0] = 1
    assert a[0] == 1
    assert len(a) == 10

test_array()