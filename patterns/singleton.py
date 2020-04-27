"""Singlton / creational"""


class SingletonDecorator(object):
    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance == None:
            self.instance = self.klass(*args, **kwargs)
        return self.klass


@SingletonDecorator
class foo: pass


x = foo()
y = foo()
z = foo()
x.val = 1
y.val = 2
z.val = 3
# print x is y is z
