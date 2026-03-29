"""
======================================
1. Создай класс SecureData, который:

имеет атрибут __secret, задаваемый в __init__;
переопределяет __getattribute__, чтобы при попытке получить __secret извне выбрасывать ValueError;
внутри класса доступ к __secret должен работать.
Проверь:
data = SecureData("пароль123")
print(data.__secret)      # ошибка
print(data.get_secret())  # "пароль123"
======================================
"""
print('Задание № 1:')

class SecureData:
    def __init__(self, secret):
        self.__secret = secret

    def get_secret(self):
        return self.__secret

    def __setattr__(self, name, value):
        print(f'Обращение к атрибуту: {name}')
        if name == 'token':
            raise ValueError('Создание атрибута "token" запрещено')
        object.__setattr__(self, name, value)

    def __getattribute__(self, item):
        if item == "__secret":
            raise ValueError("Доступ к __secret запрещён")
        return object.__getattribute__(self, item)

data = SecureData("пароль123")
# print(data.__secret)      # ошибка
print(data.get_secret())  # "пароль123"

print('-' * 33)
"""
2. Добавь в класс SecureData метод __setattr__,
который запрещает создание любого атрибута с именем token.

Проверь:
data.token = "abc123"  # ❌ AttributeError
data.other = "ok"      # ✅ работает
======================================
"""
print('Задание № 2:')

# data.token = "abc123"
data.other = "ok"

print('-' * 33)
"""
3. Создай класс SafeDict, в котором:

нет атрибута default;
реализован __getattr__, который возвращает "N/A" (это строка) при попытке получить несуществующий атрибут;
реализован __delattr__, который пишет "Удалён атрибут <имя>" и действительно удаляет атрибут.
Проверь:
d = SafeDict()
print(d.unknown)     # "N/A"
d.key = 10
del d.key            # "Удалён атрибут key"
======================================
"""
print('Задание № 3:')

class SafeDict:
    def __getattribute__(self, item):
        print(f'Обращение к атрибуту "{item}"')
        return object.__getattribute__(self, item)

    def __setattr__(self, item, value):
        print(f'Создание атрибута "{item}" со значением "{value}"')
        object.__setattr__(self, item, value)

    def __getattr__(self, name):
                return "N/A"

    def __delattr__(self, name):
        print(f'Удалён атрибут {name}')
        object.__delattr__(self, name)

d = SafeDict()
print(d.unknown)     # "N/A"
d.key = 10
del d.key            # "Удалён атрибут key"

print('-' * 33)
"""
4. Создай класс Employee с приватными полями __name и __salary.
Добавь @property для поля salary, а также сеттер с валидацией:

зарплата должна быть положительным числом;
если нет — выбрасывать ValueError.
Проверь, что:
e = Employee("Daniil", 5000)
print(e.salary)   # 5000
e.salary = 8000
print(e.salary)   # 8000
e.salary = -100   # ❌ ValueError
======================================
"""
print('Задание № 4:')

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 1:
            raise ValueError(f'Зарплата должна быть положительным числом')
        self.__salary = value

    @salary.deleter
    def salary(self):
        print('Зарплата удалена')
        del self.__salary

e = Employee("Daniil", 5000)
print(e.salary)   # 5000
e.salary = 8000
print(e.salary)   # 8000
# e.salary = -100   # ❌ ValueError

print('-' * 33)
"""
5. Добавь @deleter для поля salary, чтобы при удалении выводилось "зарплата удалена"
и поле реально исчезало.
Проверь:

del e.salary
print(e.__dict__)  # salary нет
"""
print('Задание № 5:')

del e.salary
print(e.__dict__)


print('-' * 33)
"""
6. Представь, что ты пишешь обёртку над HTML-формой.
Создай класс LoginForm с полем username, которое реализовано через @property.

Логика:
геттер возвращает self._username
сеттер добавляет лог "username изменён"
Проверь, что:
form = LoginForm()
form.username = "admin"  # выводит лог
print(form.username)     # "admin"
======================================
"""
print('Задание № 6:')

class LoginForm:

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        print('Username изменён')
        self._username = value

form = LoginForm()
form.username = "admin"  # выводит лог
print(form.username)     # "admin"


print('-' * 33)
"""
7. Создай класс Card, где:
поле __number хранит номер карты (строка);
в @property возвращай номер с маской **** **** **** 1234;
в @setter проверяй, что номер состоит из 16 цифр;
в @deleter логируй удаление номера с текущим временем.
Напиши тесты (через assert)
проверку установки корректного номера;
проверку исключения при вводе короткого номера;
проверку вывода замаскированного номера.
======================================
"""
print('Задание № 7:')

from datetime import datetime

class Card:
    def __init__(self):
        self.__number = None

    @property
    def number(self):
        if self.__number is None:
            return "Номер карты не установлен"
        return f'**** **** **** {self.__number[-4:]}'

    @number.setter
    def number(self, value):
        if not value.isdigit():
            print('Номер карты должен состоять только из цифр')
            return
        if len(value) != 16:
            print('Номер карты должен состоять из 16 цифр')
            return
        print('Карте присвоили 16 значный номер')
        self.__number = value

    @number.deleter
    def number(self):
        print(f'[LOG]: Номер карты удален - {datetime.now().strftime("%Y/%m/%d %H:%M:%S")}')
        del self.__number


karta = Card()
karta.number = '1234567890123569'
print(karta.number)
del karta.number

# !!! Как писать тесты не понял, требуется консультация
# Не понимаю как писать тест с помощью asser, напиши, пожалуйста, один пример. Дальше сделаю по аналогии.
print('-' * 33)
"""
8. Создай класс UserData для API регистрации пользователя:
email — строка, содержит @;
age — целое число ≥ 18;
is_active — bool;
свойство .json возвращает словарь для запроса.
Напиши тест (через assert)
проверь, что при age = 15 выбрасывается ValueError;
проверь, что email без @ вызывает ошибку;
проверь, что json возвращает корректную структуру.

"""
print('Задание № 8:')

class UserData:
    def __init__(self):
        self.__email = None
        self.__age = None
        self.__is_active = None

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError('Ошибка. В email должна быть "@"')
        self.__email = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError('Ошибка. Возраст должен быть числом')
        if value < 18:
            raise ValueError('Ошибка. Возраст должен быть от 18 лет')
        self.__age = value

    @property
    def is_active(self):
        return self.__is_active

    @is_active.setter
    def is_active(self, value):
        self.__is_active = value

    @property
    def json(self):
        return {
            'email': self.email,
            'age': self.age,
            'is_active': self.is_active
        }

data1 = UserData()
# Проверка того, что при age = 15 выбрасывается ValueError:
# Не понимаю как писать тест с помощью asser, напиши, пожалуйста, один пример. Дальше сделаю по аналогии.


# Проверка того, что email без @ вызывает ошибку:
# data1.email = 'adewuairu'
# Не понимаю как писать тест с помощью asser, напиши, пожалуйста, один пример. Дальше сделаю по аналогии.

# Проверка того, что json возвращает корректную структуру:
# !!! Как писать данную проверку не понял, требуется консультация
# Не понимаю как писать тест с помощью asser, напиши, пожалуйста, один пример. Дальше сделаю по аналогии.