# Создать функцию которая принимает 2 целочисленных аргумента, в теле функция выводит в консоль сумму этих чисел,
# но возвращает разность этих чисел, которую надо тоже вывести в консоль


# def func(x, y):
#     z = x + y
#     print(z)
#     z = x - y
#     return z
# x = int(input())
# y = int(input())
# print(func(x, y))




# Создать функцию которая принимает неопределённое количество целочисленных аргументов,
# и делает тоже самое только для всех переданных аргументов что и функция в задаче 1!


# def func2(numbers):
#     o = 0
#     for i in numbers:
#         o += i
#     print(o)
#     o = l[0]
#     for i in numbers[1:]:
#         o -= i
#     return o
# l = []
# while True:
#     number = input()
#     if number == 'stop':
#         print(func2(l))
#         break
#     else:
#         number = int(number)
#         l.append(number)




# Создать функцию которая принимает список размером 10 с целыми числами.
# Функция должна возвращать сумму чётных чисел этого списка


# def func3(numbers):
#     o = 0
#     for i in numbers:
#         if i % 2 == 0:
#             o += i
#     return o
# l = []
# while True:
#     if len(l) == 10:
#         print(func3(l))
#         break
#     else:
#         number = int(input())
#         l.append(number)




# Создать функцию которая принимает строку и проверяет, является ли первая буква в строке Заглавной, если нет,
# то возвращает строку с Заглавной первой буквой, если же буква заглавная то вернуть сообщение о том что в строке
# первая буква и так заглавная и ничего менять не пришлось


# def func4(stroka):
#     if stroka[0].istitle():
#         print('в строке первая буква и так заглавная и ничего менять не пришлось')
#     else:
#         new_stroka = stroka[0].upper() + stroka[1:]
#         print(new_stroka)
#         return new_stroka
#
# string = input()
# func4(string)




# Создать функцию которая принимает список длиной 10, и возвращает 2 значения  - сумма чётных чисел, и сумма нечётных
# чисел


# def func5(numbers):
#     digits = []
#     o = 0
#     p = 0
#     try:
#         for i in numbers:
#             if i.isdigit():
#                 i = int(i)
#                 digits.append(i)
#             elif '.' in i:
#                 i = float(i)
#                 digits.append(i)
#     except ValueError:
#         print('используйте точки только при вводе числа класса float')
#         return ''
#     for i in digits:
#         if i % 2 == 0:
#             o += i
#         else:
#             p += i
#     return o, p
# l = []
# while True:
#     if len(l) == 10:
#         print(func5(l))
#         break
#     else:
#         number = input()
#         l.append(number)




# Создать функцию которая проверяет, является ли слово полиндромом, и возвращает соответсвенно булево значение


# def func6(slovo):
#     if slovo[0:] == slovo[::-1]:
#         return True
#     else:
#         return False
# word = input()
# print(func6(word))




# Создать функцию конвертер валют
# курс валют : USD/BYN - 2.5, EUR/BYN - 3
# эта функция первым аргументом принимает валюту(строка) которую мы хотим конвертировать,
# вторым аргументом - валюта(тоже строка) в которую хотим перевести, третьим - сумма(число) которую
# мы хотим конвертировать. Функция должна возвращать строку с информацией вида : 100 USD  это 250 BYN
# надо реализовать возможность конвертировать как USD/BYN EUR/BYN так и наоборот - BYN/USD BYN/EUR


# def func7(valuta_in, valuta_out, summa):
#
#     try:
#         summa = float(summa)
#
#         if valuta_in == 'USD' and valuta_out == 'BYN':
#             result = summa * 2.5
#             print(f'{round(summa, 2)} {valuta_in} это {round(result, 2)} {valuta_out}')
#
#         elif valuta_in == 'BYN' and valuta_out == 'USD':
#             result = summa / 2.5
#             print(f'{round(summa, 2)} {valuta_in} это {round(result, 2)} {valuta_out}')
#
#         elif valuta_in == 'EUR' and valuta_out == 'BYN':
#             result = summa * 3
#             print(f'{round(summa, 2)} {valuta_in} это {round(result, 2)} {valuta_out}')
#
#         elif valuta_in == 'BYN' and valuta_out == 'EUR':
#             result = summa / 3
#             print(f'{round(summa, 2)} {valuta_in} это {round(result, 2)} {valuta_out}')
#
#         elif valuta_in == 'USD' and valuta_out == 'EUR':
#             print(f'На данный момент нет курса {valuta_in} -> {valuta_out} :(')
#
#         elif valuta_in == 'EUR' and valuta_out == 'USD':
#             print(f'На данный момент нет курса {valuta_in} -> {valuta_out} :(')
#
#         else:
#             print('Вы ввели недоступную валюту. Попробуйте еще раз. (Доступные валюты: USD, EUR, BYN)')
#
#     except ValueError:
#         print('Вы ввели не сумму. Попробуйте еще раз. (Сумма должна быть числом)')
#
# print()
#
# print('Доступные валюты: USD, EUR, BYN')
#
# print()
#
# exchange_in = input('Введите валюту, которую хотите конвертировать: ')
#
# exchange_out = input('Введите валюту, в которую хотите перевести: ')
#
# amount = input('Введите сумму: ')
#
# func7(exchange_in, exchange_out, amount)