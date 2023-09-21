# Напишите декоратор который будет конвертировать возвращаемое значение функции в определённый тип данных
# (можно выбрать прокинув  сам тип)



# def decorate(func):
#     def worker():
#         if tip == 'int':
#             return int(func())
#         elif tip == 'float':
#             return float(func())
#         elif tip == 'str':
#             return str(func())
#         elif tip == 'bool':
#             return bool(func())
#         elif tip == 'list':
#             return list(func())
#         elif tip == 'tuple':
#             return tuple(func())
#         elif tip == 'dict':
#             return dict(func())
#         elif tip == 'None':
#             return None
#         else:
#             raise ValueError('Такого типа нет')
#     return worker
#
# tip = input()
# @decorate
# def funct():
#     return 1
#
# print(type(funct()))



# Напишите декоратор для функции которая принимает 2 целых числа и выполняет деление этих целых чисел,
# декоратор должен перехватывать любые ошибки которые могут произойти в декорируемой функции



# def decorate(func):
#     def worker(x, y):
#         if type(x) != int or type(y) != int:
#             return 'нужно 2 целых числа (int)'
#         elif y == 0:
#             return 'на ноль делить нельзя'
#         else:
#             return x / y
#     return worker
#
# @decorate
# def funct(x, y):
#     return x / y
#
# print(funct(4,2))



# Напишите декоратор который будет запоминать в который раз вызывается функция и печатать это значение при вызове



# def decorate(func):
#     def worker():
#         global call
#         call += 1
#         return call
#     return worker
#
# @decorate
# def funct():
#     return
#
# call = 0
#
# print(funct())
# print(funct())
# print(funct())
# print(funct())

