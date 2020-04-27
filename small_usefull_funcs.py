# coding: utf-8


def one_value_generator(value):
    """Написать «вечный» генератор, который выдаёт всё время одно значение;"""
    while True:
        yield value


a = one_value_generator('cat')


# print(next(a))

def cat(*files):
    """Написать программу cat не ограничивая кол-ва файлов-аргументов;"""
    res = ''
    for file in files:
        with open(file, 'r') as f:
            res += f.read()
    print(res)


def my_xrange(*args):
    step = 1
    if any(not (type(it) is int) for it in args):
        raise TypeError

    if len(args) == 3:
        start, stop, step = args
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 1:
        stop = args[0]
        start = 0
    else:
        raise TypeError

    while (start < stop and step > 0) or (start > stop and step < 0):
        yield start
        start += step


# print(list(my_xrange(5)))

try:
    print(list(my_xrange()))
except TypeError:
    print('catch TypeError')

try:
    print(list(my_xrange(1, 0.5)))
except TypeError:
    print('catch TypeError for float')

print(list(my_xrange(5, 1, -2)))


def my_zip(*iterables):
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)


from itertools import repeat


def my_zip_longest(*args, fillvalue=None):
    iterators = [iter(it) for it in args]
    num_active = len(iterators)
    if not num_active:
        return
    while True:
        values = []
        for i, it in enumerate(iterators):
            try:
                value = next(it)
            except StopIteration:
                num_active -= 1
                if not num_active:
                    return
                iterators[i] = repeat(fillvalue)
                value = fillvalue
            values.append(value)
        yield tuple(values)


a = my_zip_longest((1, 2, 3), (4, 5, 6, 7, 8), fillvalue=0)
print(list(a))


def mix_dict(dict_to_mix):
    """Написать функцию, которая на вход принимает словарь, и возвращает словарь, в котором ключи
        со значениями поменяны местами. В случае если это невозможно сделать - выводит об этом сообщение."""
    try:
        return {value: key for key, value in dict_to_mix.items()}
    except TypeError:
        print('message for TypeError in dict')


a = {1: 'a'}
b = {1: ['a', 'c']}


# print(mix_dict(a), mix_dict(b))


def square_list(numbers):
    """ Написать короткие функции, принимающие один аргумент - список чисел, и возвращающие:
    Список квадратов чисел """
    return [x * x for x in numbers]


def second_from_list(numbers):
    """ Написать короткие функции, принимающие один аргумент - список чисел, и возвращающие:
    Каждый второй элемент списка """
    return [x for i, x in enumerate(numbers) if (i + 1) % 2 == 0]


def squres_with(numbers):
    """ Написать короткие функции, принимающие один аргумент - список чисел, и возвращающие:
    Квадраты чётных элементов на нечётных позициях.
    """
    return [x * x for i, x in enumerate(numbers) if (i + 1) % 2 == 1 and x % 2 == 0]

# a = list(range(9))
# print(square_list(a))
# print(second_from_list(a))
# print(squres_with(a))
