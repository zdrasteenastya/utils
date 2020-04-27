import types


# Option 1
class Strategy:

    def __init__(self, func=None):
        self.name = 'Patter Strategy 1'
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self):
        print(self.name)


def execute_replacement1(self):
    print(self.name + 'replace with 1')


def execute_replacement2(self):
    print(self.name + 'replace with 2')


# Option 2
from abc import abstractmethod


class People(object):
    # Strategy
    tool = None

    def __init__(self, name):
        self.name = name

    def setTool(self, tool):
        self.tool = tool

    def write(self, text):
        self.tool.write(self.name, text)


class Tools(object):
    @abstractmethod
    def write(self, *args):
        pass


class Pen(Tools):
    def write(self, *args):
        print '{} (pen) {}'.format(*args)


class Brush(Tools):
    def write(self, *args):
        print '{} (brush) {}'.format(*args)


class Student(People):
    tool = Pen()


class Painter(People):
    tool = Brush()


if __name__ == '__main__':
    strat0 = Strategy()

    strat1 = Strategy(execute_replacement1)
    strat1.name = 'Patter Strategy 2'

    strat2 = Strategy(execute_replacement2)
    strat2.name = 'Patter Strategy 3'

    strat0.execute()
    strat1.execute()
    strat2.execute()

    nik = Student('Nik')
    nik.write('write about pattern')

    sasha = Painter('sasha')
    sasha.write('draw something')
