print('Задание 6')
a = input('Введите номер билета ')
if a.isdigit() and len(a) == 6:
    b = sum(int(digit) for digit in a[0:3])
    c = sum(int(digit) for digit in a[3:])
    if b == c:
        print('Ваш билет счастливый')
    else:
        print('У вас несчастливый билет')
else:
    print('Вы ввели не номер билета')
    