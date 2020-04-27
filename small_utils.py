# coding: utf-8


class MyIterator():
    def __init__(self, data):
        self.data = data
        self.indx = -2

    def __iter__(self):
        return self

    def next(self):
        self.indx += 2
        if self.indx == len(self.data) - 2:
            raise StopIteration
        return self.data[self.indx]


a = MyIterator([1, 2, 3, 4, 5, 6, 7, 8])
for i in a:
    print i

"""
Напишите генератор odd_generator, который возвращает все нечётные
числа от 1 до n.
"""


def my_gen(l):
    for i in l:
        if i % 2 != 0:
            yield i
        else:
            continue


for a in my_gen([1, 2, 3, 4, 5, 6]):
    print a

"""
Напишите декоратор memoize, который сохраняет результат вычисления функции
и при последующих вызовах возвращает сохранённое значение, не вычисляя функцию повторно.

Предполагается, что у функции нет входных параметров (аргументов).
"""


class FunctionMock(object):
    def __init__(self, result=None):
        self.calls = 0
        self.result = result

    def __call__(self):
        self.calls += 1
        return self.result


def my_mem(f):
    cash = []

    def wrapper():
        if not cash:
            cash.append(f())
        return cash[0]

    return wrapper


fn = FunctionMock(result=1)
memoized_fn = my_mem(fn)

memoized_fn()
memoized_fn()
memoized_fn()
memoized_fn()
memoized_fn()
memoized_fn()
print fn.calls

"""
Написать функцию, которой можно передавать аргументы либо списком/кортежем, либо по одному. Функция производит суммирование всех аргументов.
"""


def f(*args):
    sum1 = 0
    for i in args:
        if hasattr(i, '__len__'):
            for el in i:
                sum1 += el
        else:
            sum1 += i
    return sum1


print f(3, (5, 6))

"""
Написать функцию-фабрику, которая будет возвращать функцию сложения с аргументом.
"""


def fabrika_sum(a):
    def add1(b):
        return a + b

    return add1


add5 = fabrika_sum(5)
print add5(3)

from functools import partial

add2 = partial(lambda x, y: x + y, 2)
print add2(1)


def fabrika_sum(a):
    return lambda x: x + a


add5 = fabrika_sum(5)
print add5(3)

"""
Написать фабрику, аналогичную п.2, но возвращающей список таких функций
"""


def fabrika_sum(a):
    return lambda x: x + a


def additional_range(start, end):
    return [(fabrika_sum(i)) for i in range(start, end)]


a = additional_range(1, 5)
for i in a:
    print i(0)

"""
Написать аналог map:

первым аргументом идет либо функция, либо список функций
вторым аргументом — список аргументов, которые будут переданы функциям
полагается, что эти функции — функции одного аргумента
"""


def fabrika_sum(a):
    return lambda x: x + a


def my_map(*args):
    res = []
    if hasattr(args[0], '__len__'):
        for f in args[0]:
            for ar in args[1]:
                res.append(f(ar))
    else:
        for ar in args[1]:
            res.append(args[0](ar))
    return res


add1 = fabrika_sum(1)
add2 = fabrika_sum(2)
add3 = fabrika_sum(3)
print my_map(add1, [0, 1])

"""
Написать функцию-генератор cycle которая бы возвращала циклический итератор.
"""


def cycle(a):
    index = -1
    while True:
        index = index + 1 if index != len(a) - 1 else 0
        yield a[index]


i = [1, 2, 3]
c = cycle(i)
print c.next()
print c.next()
print c.next()
print c.next()


class Cycle():
    def __init__(self, a):
        self.indx = -1
        self.data = a

    def __iter__(self):
        return self

    def next(self):
        self.indx = self.indx + 1 if self.indx != len(self.data) - 1 else 0
        return self.data[self.indx]


a = Cycle([1, 2, 3])
for i in a:
    print i

"""
Написать функцию-генератор chain, которая последовательно итерирует переданные объекты (произвольное количество)
"""


def my_chain(*args):
    for a in args:
        for i in a:
            yield i


for i in my_chain([1, 2, 3], [4, 5, 6]):
    print i

"""
Написать базовый класс Observable, который бы позволял наследникам:

при передаче **kwargs заносить соответствующие значения как атрибуты
сделать так, чтобы при print отображались все публичные атрибуты
"""


class Observable():

    def __init__(self, **kwargs):
        self.data = dict(kwargs)

    def __str__(self):
        return str([i for i in self.data if not i.startswith('_')])

    def __getattr__(self, item):
        return self.data[item]


class X(Observable):
    pass


x = Observable(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))
print x

print x.props

"""
Написать класс, который бы по всем внешним признакам был бы словарем, но позволял обращаться к ключам как к атрибутам.
"""


class Observable():

    def __init__(self, **kwargs):
        self.data = dict(kwargs)

    def __getattr__(self, item):
        try:
            return self.data[item]
        except KeyError:
            raise AttributeError

    def __getitem__(self, item):
        return self.data[item]


x = Observable(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))
# print x.five
print x['li']

"""
Пункт 2 с усложнением: написать родительский класс XDictAttr так, чтобы у наследника динамически определялся ключ по наличию метода get_<KEY>.
"""


class Observable():

    def __init__(self, **kwargs):
        self.data = dict(kwargs)

    def __getattr__(self, item):
        try:
            return self.data[item]
        except KeyError:
            raise AttributeError

    def __getitem__(self, item):
        return self.data[item]

    def get(self, item, default=None):
        try:
            return self.data[item]
        except KeyError:
            return default


x = Observable(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))
print x.five
print x.get('foo', 'missng')
