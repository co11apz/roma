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




