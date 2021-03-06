"""

Пусть функция atom принимает один аргумент, инициализирующий хранимое значение
(значение по умолчанию, в случае вызова atom без аргумента - None),
а возвращает 4 функции - get_value, set_value, process_value, delete_value,такие, что:


get_value - позволяет получить значение хранимой переменной;
set_value - позволяет установить новое значение хранимой переменной,
возвращает его;
process_value - принимает в качестве аргументов сколько угодно функций
и последовательно (в порядке перечисления аргументов) применяет эти функции
к хранимой переменной, обновляя ее значение (перезаписывая получившийся
результат) и возвращая получишееся итоговое значение.
delete_value - удаляет значение
"""


class Atom:

    def __init__(self, value=None):
        print('hello')
        self.__value = value

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def process_value(self, *args):
        for func in args:
            self.__value = func(self.__value)
        return self.__value

    def delete_value(self):
        self.__value = None


my_atom = Atom()

# print(my_atom.set_value(666))

a = [7,7,7,7,]

my_atom.process_value(a)

# print(my_atom.get_value())


