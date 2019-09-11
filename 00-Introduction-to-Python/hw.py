"""
Реализуйте метод, определяющий, является ли одна строка
перестановкой другой. Под перестановкой понимаем любое
изменение порядка символов. Регистр учитывается, пробелы
являются существенными.
"""

a = 'abaabaab'
b = 'abaabaab'

def is_permutation(a: str, b: str) -> bool: # первый способ
    return sorted(a) == sorted(b)


print(is_permutation('baba', 'abab'))
print(all(a.count(char) == b.count(char) for char in a)) # второй способ


print(set(a) == set(b)) # третий способ
