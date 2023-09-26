# Создать класс, и 10 экземпляров класса у которых различные значения аттрибута



# class Count:
#
#     def __init__(self, number):
#         self.number = number
#
# one = Count(1)
# two = Count(2)
# three = Count(3)
# four = Count(4)
# five = Count(5)
# six = Count(6)
# seven = Count(7)
# eight = Count(8)
# nine = Count(9)
# ten = Count(10)



# Сделать предыдущее задание через цикл



# class Count:
#
#     def __init__(self, number):
#         self.number = number
#
# for i in range(1, 11):
#     exemplar = Count(i)
#     print(exemplar.number)



# Создать экземпляр класса с 5 динамическими аттрибутами, и сделать метод который будет выводить через цикл фор
# все аттрибуты экземпляра класса



# class Account:
#
#     def __init__(self, name, surname, nickname, password, age):
#         self.name = name
#         self.surname = surname
#         self.nickname = nickname
#         self.password = password
#         self.age = age
#
#     def attributes(self):
#         for i, o in self.__dict__.items():
#             print(i, ':', o)
#
# person = Account('Bradley', 'Krueger', 'brad123', 'qwertyuiop1234', 25)
# person.attributes()



# Создать класс, у которого есть 2 статических аттрибута, и 4 динамических аттрибута,
# и реализованы 3 метода для экземпляров класса



# class Account:
#
#     site = 'site.com'
#     browser = 'Chrome'
#
#     def __init__(self, name, surname, password, age):
#         self.name = name
#         self.surname = surname
#         self.password = password
#         self.age = age
#
#     def info(self):
#         print(f'Hello, {self.name}. You now on {self.site} and your browser is {self.browser}')
#
#     def my_password(self):
#         print(f'Hello, {self.name}. Your password is {self.password}')
#
#     def nickname(self):
#         result = self.name[:3] + self.surname[:3]
#         print(f'Hello, {self.name}. The best nickname for you is {result}')
#
# person = Account('Bradley', 'Krueger', 'qwertyuiop1234', 25)



# К предыдущему классу добавить метод класса



# class Account:
#
#     site = 'site.com'
#     browser = 'Chrome'
#
#     def __init__(self, name, surname, password, age):
#         self.name = name
#         self.surname = surname
#         self.password = password
#         self.age = age
#
#     @classmethod
#     def change_browser(cls, new_browser):
#         cls.browser = new_browser
#
#     def info(self):
#         print(f'Hello, {self.name}. You now on {self.site} and your browser is {self.browser}')
#
#     def my_password(self):
#         print(f'Hello, {self.name}. Your password is {self.password}')
#
#     def nickname(self):
#         result = self.name[:3] + self.surname[:3]
#         print(f'Hello, {self.name}. The best nickname for you is {result}')
#
# person = Account('Bradley', 'Krueger', 'qwertyuiop1234', 25)
# person.change_browser('Opera')
# person.info()