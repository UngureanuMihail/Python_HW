# # Указав номер четверти прямоугольной системы координат,
# показать допустимые значения координат для точек этой четверти
choice = int(input("Укажите номер четверти прямоугольной системы координат\n"
                   "1-Для первой четверти\n"
                   "2-Для второй четверти\n"
                   "3-Для третьей четверти\n"
                   "4-Для четвёртой четверти"))
coords = []


def coord_1():
    for x in range(6):
        for y in range(6):
            coordinate = (x, y)
            coords.append(coordinate)
    return print(coords)


def coord_2():
    for x in range(-5, 0):
        for y in range(6):
            coordinate = (x, y)
            coords.append(coordinate)
    return print(coords)


def coord_3():
    for x in range(-5, 0):
        for y in range(-5, 0):
            coordinate = (x, y)
            print(coords.append(coordinate))


def coord_4():
    for x in range(6):
        for y in range(-5, 0):
            coordinate = (x, y)
            coords.append(coordinate)
    print(coords)


if choice == 1:
    coord_1()
elif choice == 2:
    coord_2()
elif choice == 3:
    coord_3()
else:
    coord_4()
