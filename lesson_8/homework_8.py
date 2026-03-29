"""
======================================
1. Создай две функции: inner() и outer().
В inner() вызови деление на ноль.
В outer() просто вызови inner().
Попробуй вызвать outer() без обработки ошибок и посмотри на стек вызовов.
======================================
"""
import copy

print('Задание № 1:')

# def inner(a, b):
#     try:
#         res = a / b
#     except ZeroDivisionError:
#         return 'Ошибка в inner'
#     else:
#         return res
#
# def outer(a, b):
#     inner(a, b)
#
# try:
#     outer(5, 0)
# except ZeroDivisionError:
#     print('Ошибка перехвачена на верхнем уровне')


print('-' * 33)
"""
2. Добавь вокруг вызова outer() конструкцию try/except,
чтобы перехватить исключение и вывести сообщение
"Ошибка перехвачена на верхнем уровне".
======================================
"""
print('Задание № 2:')

# Сделано в задании № 1

print('-' * 33)
"""
3. Перехвати исключение сразу в inner(), чтобы оно не поднималось дальше.
В случае ошибки возвращай строку "Ошибка в inner".
======================================
"""
print('Задание № 3:')

# Сделано в задании № 1

print('-' * 33)
"""
4. Сделай так:
В inner() ошибка не перехватывается.
В outer() ошибка перехватывается через try/except.
В outer() при перехвате напечатай "Ошибка в outer".
======================================
"""
print('Задание № 4:')

def inner(a, b):
    res = a / b
    return res

def outer(a, b):
    try:
        inner(a, b)
    except ZeroDivisionError:
        print('Ошибка в outer')

outer(5, 0)


print('-' * 33)
"""
5. Напиши функцию get_value(), которая кидает ValueError.
Напиши тестовую функцию test_get_value(), которая:

Вызывает get_value();
Ловит ValueError;
Завершает тест с assert False, если исключение поймано.
======================================
"""
print('Задание № 5:')

# def get_value():
#     raise ValueError
#
# def test_get_value():
#     try:
#         get_value()
#     except ValueError:
#         assert False
#
# test_get_value()

print('-' * 33)
"""
======================================
6. Создай функцию divide(x, y).
Если y == 0, выбрасывай ZeroDivisionError через raise.
Иначе возвращай результат деления.
======================================
"""
print('Задание № 6:')

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    else:
        return x / y

print(divide(10, 1))

print('-' * 33)
"""
7. Создай функцию sqrt(x), которая:
Вызывает raise NegativeNumberError (пользовательское исключение), если x < 0;
Иначе возвращает квадратный корень из x.
Проверь поведение функции через try/except.
======================================
"""
print('Задание № 7:')

class NegativeNumberError(Exception):
    '''Ошибка - отрицательное число'''

def sqrt(x):
    if x < 0:
        raise NegativeNumberError('Ошибка - отрицательное число')
    else:
        return x ** 0.5

try:
    print(sqrt(-9))
except NegativeNumberError:
    print('Ошибка, число не должно быть отрицательным')

print('-' * 33)
"""
8. Создай базовый класс MathError.
От него унаследуй:
NegativeNumberError
DivisionByZeroError
В функции safe_divide(x, y) выбрасывай DivisionByZeroError, если y == 0.
Проверь в try/except обработку ошибок через базовый класс MathError.
======================================
"""
print('Задание № 8:')

class MathError(Exception):
    pass

class NegativeNumberError(MathError):
    pass

class DivisionByZeroError(MathError):
    pass

def safe_divide(x, y):
    if y == 0:
        raise DivisionByZeroError

try:
    safe_divide(5, 0)
except MathError:
    print('Ошибка y = 0')

print('-' * 33)
"""
9. Создай тестовую функцию test_sqrt(), которая:
вызывает sqrt(x) с отрицательным числом;
перехватывает NegativeNumberError;
завершает тест с assert False и сообщением
"Нельзя брать корень из отрицательного числа".
======================================
"""
print('Задание № 9:')

# def sqrt(x):
#     if x < 0:
#         raise NegativeNumberError
#
# def test_sqrt(x):
#     try:
#         sqrt(x)
#     except NegativeNumberError:
#         assert False, 'Нельзя брать корень из отрицательного числа'
#
# test_sqrt(-77)


print('-' * 33)
"""
======================================
10. Открой файл sample.txt, прочитай его содержимое и выведи на экран.
Обеспечь закрытие файла через with.
======================================
"""
print('Задание № 10:')

with open('sample.txt', encoding='utf-8') as f:
    for line in f:
        print(line, end='')

print('\n', '-' * 33)
"""
11. Создай класс BackupList, который:
делает копию списка при входе в with,
при выходе сохраняет изменения, если ошибок не было,
откатывает изменения при ошибке.
Проверь:
успешное изменение списка;
откат при ошибке.
======================================
"""
print('Задание № 11:')

class BackupList:
    def __init__(self, lst):
        self.lst = lst
        self.copy = None

    def __enter__(self):
        self.copy = self.lst[:]
        return self.copy

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.lst.clear()
        self.lst.extend(self.copy)
        return False

lst_1 = [1, 2, 3, 4]

with BackupList(lst_1) as l_1:
    print(l_1)

try:
    lst_1.append(12)
    raise ValueError('Ошибка в работе со списком')
    lst_1.append(9)
except ValueError as v:
    print(v)
else:
    print(lst_1)


print('-' * 33)
"""
======================================
12. Создай декоратор-класс Timer,
который измеряет время выполнения функции и выводит результат.
"""
print('Задание № 12:')

import time
class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result_2 = self.func(*args, **kwargs)
        end_time = time.time()
        spend_time = end_time - start_time
        print(f"Результат вычисления функции '{self.func.__name__}' - {result_2}")
        print(f'Время выполнения функции "{self.func.__name__}" - {round(spend_time, 3)} сек.')

@Timer
def example(a, b, w):
    time.sleep(w)
    return a + b

example(4, 7, 1)