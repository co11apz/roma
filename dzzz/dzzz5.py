print('Задание 5')
a = input('Введите год ')
if a.isdigit():
    a = int(a)
    if (a % 4 == 0) and (a % 400 == 0) or (a % 4 ==0) and (a % 100 != 0):
        print('Год високосный')
    else:
        print('Год не високосный')
else:
    print('Вы ввели не год')