"""
======================================
1. Создай три класса: Cat, Dog, Duck.
В каждом реализуй метод speak(), возвращающий уникальную строку.
Создай список из экземпляров этих классов и вызови метод speak()
в цикле.
======================================
"""
print('Задание № 1:')

class Cat:
    def speak(self):
        return f'Мяу-мяу'

class Dog:
    def speak(self):
        return f'Гав-гав'

class Duck:
    def speak(self):
        return f'Кря-кря'

animals = [Cat(), Dog(), Duck()]
for animal in animals:
    print(animal.speak())


print('-' * 33)
"""
2. Создай базовый класс Shape
Создай три класса-наследника: Square, Rectangle, Triangle,
в каждом реализуй метод get_pr().
Проверь, что список shapes = [Square(...), Rectangle(...), Triangle(...)]
можно обойти в цикле и вызвать get_pr() у каждого.
======================================
"""
print('Задание № 2:')

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_pr(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_pr(self):
        return self.side * 4

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_pr(self):
        return (self.length + self.width) * 2

class Triangle(Shape):
    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def get_pr(self):
        return self.side_1 + self.side_2 + self.side_3

shapes = [Square(3), Rectangle(12, 4), Triangle(3, 5, 7)]
for shape in shapes:
    print(shape.get_pr())

print('-' * 33)
"""
3. Сделай класс Shape абстрактным.
Переопредели get_pr() как @abstractmethod.
Попробуй создать объект класса Shape напрямую и убедись, что будет TypeError.
======================================
"""
print('Задание № 3:')

# shape = Shape()

print('Убедился в том что нельзя создать объект абстрактного класса')
print("Получим TypeError: Can't instantiate abstract class Shape without an implementation for abstract method 'get_pr'")

print('-' * 33)
"""
4. Создай классы A, B, C, в каждом — свой __init__() с print("init A/B/C").
Наследуй D(A, B, C) и вызови super().__init__() в каждом __init__.
Выведи D.__mro__ и посмотри, в каком порядке вызываются инициализаторы.
======================================
"""
print('Задание № 4:')

class A:
    def __init__(self):
        super().__init__()
        print('init A')

class B:
    def __init__(self):
        super().__init__()
        print('init B')

class C:
    def __init__(self):
        print('init C')

class D(A, B, C):
    pass

d = D()
print(D.__mro__)

print('-' * 33)
"""
5. Создай MixinLog (как в уроке).
Создай класс бронирования гостиницы (методы и атрибуты на свое усмотрение).
Создай класс, который наследует оба класса. Создай экземпляр этого класса.
======================================
"""
print('Задание № 5:')

import datetime

class Booking:
    def __init__(self, name, price):
        super().__init__(name)
        print('Init Booking')
        self.name = name
        self.price = price

    def print_info(self):
        print (f'Бронь на имя: {self.name}. Стоимость номера: {self.price} Руб.')

class MixinLog:
    id = 0
    def __init__(self, name):
        print('Init MixinLog')
        MixinLog.id += 1
        self.id = MixinLog.id
        self.name = name

    def date_of_book(self):
        print(f'Бронь № {self.id} осуществлена на имя: {self.name} {datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')}')

class Holiday(Booking, MixinLog):
    pass

x = Holiday('Игорь', 12000)
x.print_info()
x.date_of_book()

print('-' * 33)
"""
6. В Goods и MixinLog реализуй print_info().
Создай NoteBook(Goods, MixinLog) и проверь, какой метод вызывается.
Измени порядок наследования — изменилась ли логика?
"""
print('Задание № 6:')

class Goods:
    def print_info(self):
        super().print_info()
        print('Printing Goods')

class MixinLog:
    def print_info(self):
        print('Printing MixinLog')

class NoteBook(Goods, MixinLog):
    pass

z = NoteBook()
z.print_info()

# При изменении порядка наследования отработает только инициализация MixinLog

print('-' * 33)
"""
======================================
======================================
Далее задания можете сделать через классы, функции или без них.
======================================
======================================
7. Напиши программу, которая запрашивает (из консоли) два числа и делит первое на второе.
Если второе число равно нулю — обработай ошибку (как называется ошибка найди сам)
и выведи сообщение: "На ноль делить нельзя!"
======================================
"""
# print('Задание № 7:')
#
# try:
#     a, b = map(float, input("Введите два числа через пробел: ").split())
#     x = a / b
# except ZeroDivisionError as z:
#     print('На ноль делить нельзя!\n'
#           f'ОШИБКА!!! - ZeroDivisionError: {z}')
# except ValueError as v:
#     print('Ошибка ввода: введите два числа через пробел\n'
#           f'ОШИБКА!!! - ValueError: {v}')
# except Exception as e:
#     print('Произошла неизвестная ошибка')
# else:
#     print(f'Результат деления = {x}')
#
# print('-' * 33)
"""
8. Расширь программу из Задания 1:
Добавь обработку ошибки (как называется ошибка найди сам),
если пользователь ввёл не числа, а текст.
Выведи сообщение: "Ошибка ввода: введите два числа через пробел"
======================================
"""
print('Задание № 8:')

# Расширил задание № 7 обработкой ошибки ввода текста вместо числа
# См. результат  выполнения задания № 7


print('-' * 33)
"""
9. Модифицируй код так, чтобы после обработки конкретных ошибок
был ещё один общий except, который перехватывает все остальные ошибки и выводит:
"Произошла неизвестная ошибка"
======================================
"""
print('Задание № 9:')

# Модифицировал код, добавил общий except.
# Но вызвать его не получается, т.к. ValueError и ZeroDivisionError покрывают все возможные ошибки.
# См. результат  выполнения задания № 7

print('-' * 33)
"""
10. При перехвате исключений из 7 и 8 заданий,
сохрани ошибку в переменную e и выведи её текст:
======================================
"""
print('Задание № 10:')

# Сделано.
# См. результат  выполнения задания № 7

print('-' * 33)
"""
11. Создай код, который ловит арифметические ошибки (ArithmeticError) в одном блоке.
Попробуй специально сделать ошибку деления на ноль или другую арифметическую ошибку.
======================================
"""
print('Задание № 11:')

try:
    result = 155 / 0
except ArithmeticError as a:
    print(f'Арифметическая ошибка: {a}')

print('-' * 33)
"""
12. Запроси у пользователя два числа и выполни деление.
Если деление прошло успешно без ошибок — выведи
"Деление выполнено успешно" через (но не в блоке try)
======================================
"""
# print('Задание № 12:')
#
# success = False
#
# try:
#     num_1 = int(input('Введите первое число: '))
#     num_2 = int(input('Введите второе число: '))
#     result_2 = num_1 / num_2
#     print(f'Результат деления: {result_2}')
#     success = True
# except ArithmeticError as b:
#     print(f'Арифметическая ошибка: {b}')
#
# if success:
#     print('Деление выполнено успешно')
#
# print('Работа программы завершена')
#
# print('-' * 33)
"""
13. Расширь код из Задания 12:
Добавь блок, в котором будет выводиться
"Работа программы завершена", независимо от успеха деления.
======================================
"""
print('Задание № 13:')

# Блок добавлен в задание № 12

print('-' * 33)
"""
14. Реализуй две вложенные конструкции:
Внешний try/except обрабатывает неверный ввод (строки вместо чисел);
Внутренний try/except ловит деление на ноль.
======================================
"""
# print('Задание № 14:')
#
# try:
#     num_3 = int(input('Введите первое число: '))
#     num_4 = int(input('Введите второе число: '))
# except ValueError:
#     print(f'Ошибка. Введена строка вместо числа')
# else:
#     try:
#         res = num_3 / num_4
#     except ZeroDivisionError:
#         print(f'Ошибка. Нельзя делить на ноль')
#     else:
#         print(f'Результат деления: {res}')
#
# print('-' * 33)
"""
15. Вынеси обработку деления в отдельную функцию divide(x, y)
с собственным try/except.
Во внешнем коде обработай только ошибку ввода.
"""
print('Задание № 15:')

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print(f'Ошибка. Нельзя делить на ноль')
    else:
        print(f'Результат деления: {result}')


try:
    num_3 = int(input('Введите первое число: '))
    num_4 = int(input('Введите второе число: '))
except ValueError:
    print(f'Ошибка. Введена строка вместо числа')
else:
    divide(num_3, num_4)

