from random import randint as ri

# 3. Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного int

# n = int(input('Введите кол-во чисел: '))
# f = lambda i: ri(0,20)
# my_list = []
# for i in range(n):
#     my_list.append(ri(0, 20))
# print(my_list)
# for i in range(n):
#     indeks = ri(0, n-1)
#     z = my_list[i]
#     my_list[i] = my_list[indeks]
#     my_list[indeks] = z
# print(my_list)

n = int(input('Введите кол-во чисел: '))
my_list = list(map(lambda i: ri(0,20), [i for i in range(n)]))
print(my_list)
for i in range(n):
    indeks = ri(0, n-1)
    z = my_list[i]
    my_list[i] = my_list[indeks]
    my_list[indeks] = z
print(my_list)

# 2. Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# n = int(input('Введите число '))
# my_list = []
# sum=0
# for i in range(1,n+1):
#     z = round((1 + 1/i)**i,2)
#     my_list.append(z)
#     sum += z
# print(f'Для n = {n} -> {my_list}')
# print(f'Сумма {sum}')

n = int(input('Введите число '))
sum = 0
my_list1 = list(map(lambda i:round((1+1/i)**i,2), [i for i in range(1,n+1)]))
for i in range(len(my_list1)):
    sum += my_list1[i]
print(f'Для n = {n} -> {my_list1}')
print(f'Сумма {sum}')
