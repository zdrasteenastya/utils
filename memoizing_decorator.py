# coding: utf-8

"""
Напишите декоратор memoize, который сохраняет результат вычисления функции
и при последующих вызовах возвращает сохранённое значение, не вычисляя функцию повторно.

Предполагается, что у функции нет входных параметров (аргументов).
"""


def memoize(fn):
    cache = []

    def wrapped():
        if fn.calls == 0:
            cache.append(fn())
            return cache[0]
        else:
            return cache[0]

    return wrapped


# ---------------------------------------
# Тесты для проверки правильности решения
import unittest

class FunctionMock(object):

    def __init__(self, result=None):
        self.calls = 0
        self.result = result

    def __call__(self):
        self.calls += 1
        return self.result

class MemoizeTest(unittest.TestCase):

    def test_function_is_called(self):
        fn = FunctionMock()
        memoized_fn = memoize(fn)

        memoized_fn()

        self.assertEqual(fn.calls, 1)

    def test_function_is_called_once(self):
        fn = FunctionMock(result=1)
        memoized_fn = memoize(fn)

        memoized_fn()
        memoized_fn()

        self.assertEqual(fn.calls, 1)

    def test_function_result(self):
        fn = FunctionMock(result=10)
        memoized_fn = memoize(fn)

        result = memoized_fn()

        self.assertEqual(result, fn.result)

    def test_function_that_returns_none(self):
        fn = FunctionMock()
        memoized_fn = memoize(fn)

        result = memoized_fn()
        result = memoized_fn()

        self.assertEqual(fn.calls, 1)
        self.assertEqual(result, fn.result)


unittest.main()
