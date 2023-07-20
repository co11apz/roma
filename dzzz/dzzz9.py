print('Задание 9')
a = input('Введите ваш пароль ')

has_uppercase = any(char.isupper() for char in a)
has_lowercase = any(char.islower() for char in a)
has_digit = any(char.isdigit() for char in a)
has_special = any(char for char in a if not char.isalnum())

if len(a) >= 6 and has_uppercase and has_lowercase and has_digit and has_special:
    print('Ваш пароль надёжный')
else:
    print('Ваш пароль не надёжный')
