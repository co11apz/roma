print('Задание 7')
a = input('Введите ваше имя ')
if a.isalpha() and a.istitle():
    print(f'Ваше имя: {a}')
else:
    print('Вы ввели не имя, либо ввели его с маленькой буквы')
