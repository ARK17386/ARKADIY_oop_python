"""
======================================
1. Создай класс Person с методом set_data(self, name, age), который сохраняет имя и возраст в объект.
Добавь метод get_data(self), который возвращает строку вида "Имя: <name>, Возраст: <age>".
Создай два объекта и задай им разные значения. Выведи информацию по каждому.
======================================
"""
print('Задание № 1:')

class Person:
    def set_data(self, name, age):
        self.name = name
        self.age = age

    def get_data(self):
        return f'Имя: {self.name}, Возраст: {self.age}'


person_1 = Person()
person_2 = Person()

person_1.set_data('Иван', 17)
print(person_1.get_data())
person_2.set_data('Геннадий', 26)
print(person_2.get_data())


print('-' * 33)
"""
2. Добавь в класс Point методы set_coords(x, y) и get_coords().
Создай объект p, задай координаты (7, 12), а затем получи и выведи их.
После этого измени координаты на (-3, 5) и снова выведи результат через get_coords().
======================================
"""
print('Задание № 2:')

class Point:
    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

p = Point()
p.set_coords(7, 12)
print(p.get_coords())

setattr(p, 'x', -3)
setattr(p, 'y', 5)
print(p.get_coords())

print('-' * 33)
"""
3. Используя getattr(), получи ссылку на метод get_coords у объекта Point и вызови его.
Проверь, что результат совпадает с обычным вызовом p.get_coords().
======================================
"""
print('Задание № 3:')

result_1 = getattr(p, 'get_coords')
print('Через getattr: ', result_1())
print('Через p.get_coords: ', p.get_coords())

print('-' * 33)
"""
4. Создай класс Person, в котором метод __init__() принимает имя и возраст и сохраняет их как атрибуты объекта.
Добавь метод show_info(), который выводит строку "Имя: <name>, возраст: <age>". Создай объект и вызови метод.
======================================
"""
print('Задание № 4:')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f'Имя: {self.name}, возраст: {self.age}')

person_3 = Person('Григорий', 24)
person_3.show_info()
# print(person_3.__dict__)

print('-' * 33)
"""
5. Добавь в класс Person метод __del__(), который выводит сообщение "Удалён объект: <имя>",
где <имя> — значение поля name. Создай и удали объект вручную с помощью del.
======================================
"""
print('Задание № 5:')

class Person_2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f'Удалён объект: {self.name}')

person_4 = Person_2('Анатолий', 33)
del person_4

print('-' * 33)
"""
6. Создай класс Rectangle с инициализацией по умолчанию: ширина 1, высота 1.
Добавь метод area(), который возвращает площадь прямоугольника.
Проверь работу с прямоугольником без аргументов и с заданной шириной и высотой.
======================================
"""
print('Задание № 6:')

class Rectangle:
    def __init__(self, width: int = 1, height: int = 1):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rectangle_1 = Rectangle()
print('Площадь прямоугольника 1:', rectangle_1.area())

rectangle_2 = Rectangle(3, 5)
print('Площадь прямоугольника 2:', rectangle_2.area())

print('-' * 33)
"""
7. Создай класс Logger, который всегда возвращает один и тот же объект.
При создании экземпляра в __new__ выводи Создание логгера,
а при вызове __init__ — Инициализация логгера.
======================================
"""
print('Задание № 7:')

class Logger:
    instance = None

    def __new__(cls, *args, **kwargs):
        print('Создание логгера')
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        print('Инициализация логгера')

logger_1 = Logger()
logger_2 = Logger()
logger_3 = Logger()
print(id(logger_1), id(logger_2), id(logger_3))