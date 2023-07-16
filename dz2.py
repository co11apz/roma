print('Задание 2')
print('Введите три числа')
a = input("Введите 1 число: ")
if a.isalpha():
    print('Ошибка, вы ввели не число')
    exit()
else: print('Первое число:', a)
b = input("Введите 2 число: ")
if b.isalpha():
    print('Ошибка, вы ввели не число')
    exit()
else: print('Второе число:', b)
c = input("Введите 3 число: ")
if c.isalpha():
    print('Ошибка, вы ввели не число')
    exit()
else: print('Третье число:', c)
choice = input("Выберите действие (максимум, минимум, среднее): ")
if choice == "максимум":
 maximum = max(float(a), float(b), float(c))
 print(f"Максимум из трех чисел: {maximum}")
elif choice == "минимум":
 minimum = min(float(a), float(b), float(c))
 print(f"Минимум из трех чисел: {minimum}")
elif choice == "среднее":
 average = (float(a) + float(b) + float(c)) / 3
 print(f"Среднеарифметическое трех чисел: {average}")
else:
 print("Ошибка")