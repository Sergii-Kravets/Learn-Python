"""
Напишите функцию modified_func, которая принимает функцию (обозначим ее func),
а также произвольный набор позиционных (назовем их fixated_args) и именованных
(назовем их fixated_kwargs) аргументов и возвращает новую функцию,
которая обладает следующими свойствами:

1.При вызове без аргументов повторяет поведение функции func, вызванной
с fixated_args и fixated_kwargs.
2.При вызове с позиционными и именованными аргументами дополняет ими
fixed_args (приписывает в конец списка fixated_args), и fixated_kwargs
(приписывает новые именованные аргументы и переопределяет значения старых)
и далее повторяет поведение func с этим новым набором аргументов.
3.Имеет __name__ вида func_<имя функции func>
4.Имеет docstring вида:

A func implementation of <имя функции func>
with pre-applied arguments being:
<перечисление имен и значений fixated_args и fixated_kwargs>
source_code:
   ...


Для того, чтобы получить имена позиционных аргументов и исходный код, советуем использовать
возможности модуля inspect.

Попробуйте применить эту функцию на написанных функциях из дз1, дз2, дз3. К функциям min, max, any() ?
decorator
"""

def func(*args, **kwargs):
    return print(args, kwargs)


def partial(func, *fixated_args, **fixated_kwargs):
    def new_func(*new_func_args, **new_func_kwargs):
        if new_func_args and new_func_kwargs:
            fixated_kwargs.update(**new_func_kwargs)
            return func(*fixated_args.__add__(new_func_args), **fixated_kwargs)
        else:
            return func(*fixated_args, **fixated_kwargs)

    return new_func


example_func = partial(func, 2, 2, 2, **{"very_very_nice": 222})

example_func(33, 33, 33, **{"very_nice": 333444})
example_func(33, 33123, 33, **{"very_very_nice": 0})
