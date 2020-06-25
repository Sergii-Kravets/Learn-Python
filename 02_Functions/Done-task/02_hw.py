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


def atom(argument=None):
    if argument is None:
        return None

    def get_value():
        nonlocal argument
        return argument

    def set_value(new_argument):
        nonlocal argument
        argument = new_argument
        return argument

    def delete_value():
        nonlocal argument
        argument = None

    def process_value(*func):
        global new_argument
        nonlocal argument
        new_argument = argument

        for i in func:
            new_argument = i(argument)

        return new_argument

    return get_value, set_value, process_value, delete_value


print(atom())

get_x, set_x, process_x, delete_x = atom('Hello python')
assert get_x() == 'Hello python'
assert process_x() == 'Hello python'
assert process_x(lambda x: x[::-1], ) == 'nohtyp olleH'
assert set_x(10) == 10
delete_x()
assert not get_x()

get_x, set_x, process_x, delete_x = atom("Sergii")
assert get_x() == "Sergii"
assert set_x("Igor") == "Igor"
print(process_x(lambda x: x[::-1]))
assert process_x(lambda x: x[::-1], ) == 'rogI'
delete_x()
assert not get_x()
