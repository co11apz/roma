a = input()
a = float(a) or int(a)
if type(a) is float:
    print('+')
else:
    print('-')