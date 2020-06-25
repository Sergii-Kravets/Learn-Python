"""Напишите реализацию функции make_it_count, которая принимает в качестве
аргументов некую функцию (обозначим ее func) и имя глобальной переменной
(обозначим её counter_name), возвращая новую функцию, которая ведет себя
в точности как функция func, за тем исключением, что всякий раз при вызове
инкрементирует значение глобальной переменной с именем counter_name.
"""

counter_name = 0


def make_it_count(func):
    global counter_name

    same = func

    def same_func():
        global counter_name
        counter_name += 1
        return func()

    return same_func


def func():
    return 1 + 1


print(func())

print(make_it_count(func))

a = make_it_count(func)

print(a())

a()
a()
a()
a()
a()
a()

print(counter_name)
