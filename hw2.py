#Напишите программу, которая принимает на вход координаты точки (X и Y), 
#причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится). 



def koord(x):
    a = [0] * x
    for i in range(x):
        b = False
        while not b:
            try:
                number = float(input(f"Введите {i+1} координату: "))
                a[i] = number
                b = True
                if a[i] == 0:
                    b = False
                    print("Координата равна 0!! ")
            except ValueError:
                print("Вводить только числа!")
    return a


def checkKoord(d):
    msg = 4
    if d[0] > 0 and d[1] > 0:
        msg = 1
    elif d[0] < 0 and d[1] > 0:
        msg = 2
    elif d[0] < 0 and d[1] < 0:
        msg = 3
    print(f"Точка находится в {msg} четверти плоскости")


koordinate = koord(2)
checkKoord(koordinate)