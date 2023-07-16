
a = input('Введите число: ')
if a.isdigit() or (a.startswith('-') and a[1:].isdigit()):
    a = float(a)
    if a > 0:
        print('Ваше число положительное')
    elif a < 0:
        print('Ваше число отрицательное')
    else:
        print('Ваше число равняется нулю')
else:
    print('Вы ввели не число')
