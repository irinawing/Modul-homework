'''
Домашнее задание по теме "Интроспекция"
Цель задания:

Закрепить знания об интроспекции в Python.
Создать персональную функции для подробной интроспекции объекта.

Задание:
Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
  - Другие интересные свойства объекта, учитывая его тип (по желанию).


Пример работы:
number_info = introspection_info(42)
print(number_info)

Вывод на консоль:
{'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}

Рекомендуется создавать свой класс и объект для лучшего понимания
'''

import inspect
from pprint import pprint
from types import ModuleType
from typing import Dict, Union, Any, List


def introspection_info(obj):
    result: dict[str, Union[Union[str, list[str], ModuleType, None], Any]] = {
        'Type': type(obj),
        'Attribute': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
        'Method': [method for method in dir(obj) if callable(getattr(obj, method))],
        'Module': inspect.getmodule(obj),
        'Module_name': introspection_info.__module__,
        'Func_name': introspection_info.__name__,
        'id_object': id(obj)
    }
    return result


class Student:

    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.info()

    def info(self):
        print(f'My name {self.name}, I am a {self.school} student')


number_info1 = introspection_info(42)
pprint(number_info1)
print()
print('----------------------------------------------------------------------------')
print()
number_info2 = introspection_info(Student('Vyacheslav', 'Urban university'))
pprint(number_info2)