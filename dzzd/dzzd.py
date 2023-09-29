# Напишите декоратор который будет конвертировать возвращаемое значение функции в определённый тип данных
# (можно выбрать прокинув  сам тип)



# def decorate(func):
#
#     def worker(tip):
#
#         if tip == int:
#             return int(func(tip))
#         elif tip == float:
#             return float(func(tip))
#         elif tip == str:
#             return str(func(tip))
#         elif tip == bool:
#             return bool(func(tip))
#         elif tip == list:
#             return [func(tip)]
#         elif tip == tuple:
#             return (func(tip),)
#         elif tip == dict:
#             return {'dict': func(tip)}
#         elif tip == None:
#             return None
#         else:
#             raise NameError
#     return worker
#
#
# @decorate
# def funct(type):
#     return 1
# try:
#     print(type(funct(dict)))
# except NameError:
#     print('Некорректный тип данных')
# except TypeError:
#     print('Введите тип данных')



# Напишите декоратор для функции которая принимает 2 целых числа и выполняет деление этих целых чисел,
# декоратор должен перехватывать любые ошибки которые могут произойти в декорируемой функции



def decorate(func):
    def worker(x, y):
        return x / y
    return worker

@decorate
def funct(x, y):
    return x / y

try:
    print(funct(4,2))

except TypeError:
    print('Введите 2 числа')

except ZeroDivisionError:
    print('На ноль делить нельзя')

except NameError:
    print('Вы ввели не число')



# Напишите декоратор который будет запоминать в который раз вызывается функция и печатать это значение при вызове



# def decorate(func):
#     call = 0
#     def worker():
#         nonlocal call
#         call += 1
#         print(call)
#         return call
#
#     return worker
#
# @decorate
# def funct():
#     return
#
#
#
# funct()
# funct()
# funct()
# funct()

