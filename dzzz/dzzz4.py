print('Задание 4')
a = input('Введите первое число ')
b = input('Введите второе число ')
c = input('Введите третье число ')
if a.isdigit() and b.isdigit() and c.isdigit():
    a = int(a)
    b = int(b)
    c = int(c)
    d = (a, b, c)
    print('Минимальное из трех чисел', min(d))
    print('Максимальное из трех чисел', max(d))
else:
    print('Ошибка. Вы ввели не число в одной или в нескольких переменных')