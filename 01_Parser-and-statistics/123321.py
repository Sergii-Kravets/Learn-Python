# def fib(n):
#     fib1 = fib2 = 1
#     i = 2
#     while i < n:
#         fib_sum = fib2 + fib1
#         fib1 = fib2
#         fib2 = fib_sum
#         i += 1
#     return fib_sum;
#
#
# a = n = int(input())
#
# print(fib(a))

n = int(input('Какой член ряда Фибоаччи вам нужен?'))
j = 1
k = 0
l = 0
for i in range(1, n + 1):
    l = j + k
    j = k
    k = l
print(l)
