print('Задание 1')
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
choice = input("Выберите действие (sum or multpl): ")
if choice == "sum":
 result = float(a) + float(b) + float(c)
 print("Сумма трех чисел:", result)
elif choice == "multpl":
 result = float(a) * float(b) * float(c)
 print("Произведение трех чисел:", result)
else:
 print("Ошибка")






