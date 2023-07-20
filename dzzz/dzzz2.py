print('Задание 2')
a = input('Введите номер месяца ')
if a.isdigit():
    a = int(a)
    if a in range(1, 13):
        if a in (3, 4, 5):
            print('Пора года: весна')
        elif a in (6, 7, 8):
            print('Пора года: лето')
        elif a in (9, 10, 11):
            print('Пора года: осень')
        else:
            print('Пора года: зима')
    else:
        print('Число не соответствует месяцу')
else:
    print('Вы ввели не число')