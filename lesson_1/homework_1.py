"""
++++++++++++++++++++++++++++++++++++++
Классы и атрибуты
++++++++++++++++++++++++++++++++++++++
======================================
1. Создай класс Dog с атрибутами класса species = "canis" и legs = 4.
Затем создай два объекта этого класса и измени у одного из них локальный атрибут.
Проверь, как это повлияло на значения у обоих объектов.
Убедись, что __dict__ объектов отражает изменения.
"""
print('Задание № 1:')
class Dog:
    'Класс для создания собак'
    species = "canis"
    legs = 4

bobik = Dog()
sharik = Dog()

bobik.species = 'superdog'

print('Разновидность Бобика:', bobik.species)
print('Кол-во ног у Бобика:', bobik.legs)
print()
print('Разновидность Шарика:', sharik.species)
print('Кол-во ног у Шарика:', sharik.legs)
print()
print('Атрибуты Бобика: ', bobik.__dict__)
print('Атрибуты Шарика: ', sharik.__dict__)

print('----------------------------------------')
"""

2. Добавь в класс Dog строку документации, описывающую его назначение.
Затем выведи её на экран.
После этого добавь в объект класса новые атрибуты name и age,
а затем удали name.
Проверь, что произойдёт при попытке снова вывести объект.name.
"""
print('Задание № 2:')
print(Dog.__doc__)

setattr(Dog, 'name', 'Tuzik')
setattr(Dog, 'age', 8)

print(getattr(Dog, 'name'))
print(getattr(Dog, 'age'))
print()
del Dog.name
# print(getattr(Dog, 'name')) # При попытке снова вывести объект.name, получаем ошибку: AttributeError: type object 'Dog' has no attribute 'name'
print(getattr(Dog, 'name', 'Значение не найдено'))

print('----------------------------------------')
"""

3. Создай класс User с атрибутами класса role = "guest" и active = True.
С помощью функций getattr(), setattr(), hasattr() и delattr():

измени значение role на "admin",
проверь наличие active,
добавь новый атрибут email,
удали role.
Убедись, что всё работает корректно, и выведи итоговое содержимое __dict__ класса User.
"""
print('Задание № 3')
class User:
    role = 'guest'
    active = True

setattr(User, 'role', 'admin')
print('Новое значение role -', getattr(User, 'role'))
print('Наличие active:', hasattr(User, 'active'))

setattr(User, 'email', '123@yamail.ru')

delattr(User, 'role')
if hasattr(User, 'role'):
    print('role - не удален')
else:
    print('role - удален')

print(User.__dict__)




