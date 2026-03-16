"""
======================================
1. Создай класс Circle, в котором:
есть атрибуты класса MIN_RADIUS = 1 и MAX_RADIUS = 1000,
метод класса is_valid_radius(cls, r), который проверяет, входит ли значение в допустимый диапазон.
Проверь результат вызова:
print(Circle.is_valid_radius(500))   # True
print(Circle.is_valid_radius(1500))  # False
======================================
"""


print('Задание № 1:')

class Circle:
    MIN_RADIUS = 1
    MAX_RADIUS = 1000

    def __init__(self, radius):
        if not self.is_valid_radius(radius):
            raise ValueError('Радиус не входит в допустимый диапазон')
        self.radius = radius

    @classmethod
    def is_valid_radius(cls, r):
        return cls.MIN_RADIUS <= r <= cls.MAX_RADIUS

    @staticmethod
    def area(radius):
        return pi * radius ** 2

    def print_info(self):
        print(f'Радиус: {self.radius}')
        print(f'Допустимый диапазон: [{type(self).MIN_RADIUS}, {type(self).MAX_RADIUS}]')

print(Circle.is_valid_radius(500))
print(Circle.is_valid_radius(1500))

print('-' * 33)
"""
2. Добавь в класс Circle:
статический метод area(radius),
который возвращает площадь круга по формуле π * r ** 2 (используй импорт math.pi),
инициализацию в __init__, которая сохраняет радиус,
только если он проходит валидацию через метод is_valid_radius()
(подумай как можно проверить значения перед тем как записать их в переменные экземпляра класса)
Пример:
c = Circle(10)
print(c.area(c.radius))  # Площадь круга
======================================
"""
print('Задание № 2:')

from math import pi

c = Circle(10)
print(round(c.area(c.radius), 6))
# Статический метод и инит добавил в задании № 1, т.к. если добавить тут - возвращается ошибка.
# Видимо их нужно добавлять вначале под классом.
print('-' * 33)
"""
3. Расширь Circle, добавив обычный метод print_info, который выводит:
Радиус: ...
Допустимый диапазон: [MIN, MAX]
Метод должен использовать и self, и атрибуты класса через type(self).

Пример вызова:
c.print_info()
======================================
"""
print('Задание № 3:')
# Метод добавил в задании № 1
c.print_info()

print('-' * 33)
"""
4. Создай класс User, в котором:

приватные атрибуты __login и __password;
метод set_credentials(login, password), который сохраняет их только если оба значения — строки;
метод get_credentials(), который возвращает кортеж из логина и пароля.
Попробуй создать объект и изменить логин снаружи напрямую. Проверь, что это не сработает.
======================================
"""
print('Задание № 4:')

class User:

    # def set_credentials(self, login, password):
    #     if isinstance(login, str) and isinstance(password, str):
    #         self.__login = login
    #         self.__password = password

    def set_credentials_2(self, login, password):
        if isinstance(login, str) and isinstance(password, str):
            self.__login = login
            self.__password = self.__encrypt_password(password)

    def get_credentials(self):
        return self.__login, self.__password

    # def check_password(self, password):
    #     if self.__password == password:
    #         return True
    #     else:
    #         return False

    def check_password_2(self, password):
            return self.__password == self.__encrypt_password(password)

    def __encrypt_password(self, password):
        return password.upper()

    def get_password(self):
        return self.__password


user1 = User()
user1.set_credentials_2("Petrov", "Ytrewq")
print(user1.get_credentials())

user1.__login = "Sidorov"
print(user1.get_credentials()) # Изменение логина снаружи не сработало


print('-' * 33)
"""
5. Добавь в User:

метод check_password(password) — возвращает True,
если переданное значение совпадает с сохранённым паролем;
приватный метод __encrypt_password(password),
который возвращает пароль в верхнем регистре (имитация шифрования);
в set_credentials вызывай __encrypt_password.
Пример:
u = User()
u.set_credentials("daniil", "qwerty")
print(u.check_password("qwerty"))      # True
print(u.check_password("qwe"))         # False
======================================
"""
print('Задание № 5:')
# В этом задании создал методы: set_credentials_2 и check_password_2, чтобы не нарушалось выполнение 4-го задания.
u = User()
u.set_credentials_2("daniil", "qwerty")
print(u.check_password_2("qwerty"))
print(u.check_password_2("qwe"))

print('-' * 33)
"""
6. Убедись, что приватный метод __encrypt_password нельзя вызвать извне.
Попробуй это сделать — и поясни результат.
Также выведи напрямую u.__password — и проверь, что будет ошибка.

Попробуй добраться до данных через u._User__password
"""
print('Задание № 6:')

# u.__encrypt_password('sdvgs') # Метод не вызывается так как он приватный. Да и как его шифровать, другим паролем?
# print(u.__password) # Ошибка. Атрибут объекта класса защищенный.

# print(u.get_password())
print(u.__dict__)
print(u._User__password)

