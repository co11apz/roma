print('Задание 9')
a = input('Введите ваш пароль ')
b = any(char.isupper() for char in a)
c = any(char.islower() for char in a)
d = any(char.isdigit() for char in a)
e = any(char for char in a if not char.isalnum())
if len(a) >= 6 and b and c and d and e:
    print('Ваш пароль надёжный')
else:
    print('Ваш пароль не надёжный')
