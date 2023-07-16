print('Задание 3')
def convert_units():
    mt = float(input("Введите количество метров: "))
    choice = input("Выберите единицы измерения (мили, дюймы, ярды): ")
    if choice == "мили":
        ml = mt * 0.000621371
        print(f"{mt} метров = {ml} миль")
    elif choice == "дюймы":
        inch = mt * 39.3701
        print(f"{mt} метров = {inch} дюймов")
    elif choice == "ярды":
        yar = mt * 1.09361
        print(f"{mt} метров = {yar} ярдов")
    else:
        print("Ошибка")
convert_units()
