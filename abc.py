import collections as c


class MyContainer(c.Container):
    def __init__(self, a):
        self.a = [a]

    def __contains__(self, item):
        return True if item in self.a else False


v = MyContainer(2)

print 2 in v

print isinstance([1, 2, 3], c.Set)  # False
print isinstance([1, 2, 3], c.Container)  # True


class MyIterator(c.Iterator):

    def __init__(self, list1):
        self.list = list1
        self.len = len(list1)
        self.index = -1

    def next(self):
        if self.len - 2 == self.index:
            raise StopIteration
        self.index += 1
        return self.list[self.index]


for i in MyIterator([1, 2, 3]):
    print i
