# 1)Создать функцию которая на вход получает произвольный список из чисел как аргумент, эта функция должна вернуть
# другую функцию, которая принимает один аргумент - число и возвращает список. Возвращаемый список должен состоять
# из всех элементов первого списка умноженных на число. Исходный список нельзя мутировать

# def func(spisok):
#     def inner_func(z):
#         new_l = []
#         for i in spisok:
#             i = int(i)
#             x = i * z
#             new_l.append(x)
#         return new_l
#     return inner_func
#
# l = [1, 2, 3, 4]
# b = func(l)
# print(b(4))

# 2)Cоздайте функцию add(n), при вызове которой добавляет n к числу, например :
# add_one = add(1)
# add_one(3) »»»4
# add_three = add(3)
# add_three(4) »»»7

# def add(n):
#     def inner_add(z):
#         return n + z
#     return inner_add
#
# add_one = add(1)
# print(add_one(3))


# 3)Создайте функцию _if, которая принимает 3 аргумента  - булево значение, и 2 функции (которые не принимают значений)
# - func1 и func2, когда булево значение в функции _if - истинно, то вызывается функция func1
# и выводит на экран »»»True, когда ложна - вызывается func2 и выводит »»» False

# def func1():
#     return 'True'
# def func2():
#     return 'False'
# def _if(bol, fun, fun2):
#     if bol == True:
#         return fun
#     else:
#         return fun2
# print(_if(True, func1(), func2()))