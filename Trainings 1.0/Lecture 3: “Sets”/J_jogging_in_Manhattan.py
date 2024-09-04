"""
J. Пробежки по Манхэттену
Ограничение времени	2 секунды
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Дороги Нью-Манхэттена устроены следующим образом. С юга на север через каждые сто метров проходит авеню, с запада на
восток через каждые сто метров проходит улица. Авеню и улицы нумеруются целыми числами. Меньшие номера соответствуют
западным авеню и южным улицам. Таким образом, можно построить прямоугольную систему координат так, чтобы точка (x, y)
лежала на пересечении x-ой авеню и y-ой улицы. Легко заметить, что для того, чтобы в Нью-Манхэттене дойти от точки
(x1, y1) до точки (x2, y2) нужно пройти |x2 − x1| + |y2 − y1| кварталов. Эта величина называется манхэттенским
расстоянием между точками (x1, y1) и (x2, y2).

Миша живет в Нью-Манхэттене и каждое утро делает пробежку по городу. Он выбегает из своего дома, который находится в
точке (0, 0) и бежит по случайному маршруту. Каждую минуту Миша либо остается на том же перекрестке, что и минуту
назад, или перемещается на один квартал в любом направлении. Чтобы не заблудиться Миша берет с собой навигатор,
который каждые t минут говорит Мише, в какой точке он находится. К сожалению, навигатор показывает не точное положение
Миши, он может показать любую из точек, манхэттенское расстояние от которых до Миши не превышает d.

Через t × n минут от начала пробежки, получив n-е сообщение от навигатора, Миша решил, что пора бежать домой.
Для этого он хочет понять, в каких точках он может находиться. Помогите Мише сделать это.

Формат ввода
Первая строка входного файла содержит числа t, d и n (1 ≤ t ≤ 100, 1 ≤ d ≤ 100, 1 ≤ n ≤ 100).

Далее n строк описывают данные, полученные от навигатора. Строка номер i содержит числа xi и yi — данные, полученные
от навигатора через ti минут от начала пробежки.

Формат вывода
В первой строке выходного файла выведите число m — число точек, в которых может находиться Миша. Далее выведите
m пар чисел — координаты точек. Точки можно вывести в произвольном порядке.

Гарантируется, что навигатор исправен и что существует по крайней мере одна точка, в которой может находиться Миша.
"""
# TODO доработать неисправный случай
import random


def extend(rect, d):
    minPlus, maxPlus, minMinus, maxMinus = rect
    return [minPlus - d, maxPlus + d, minMinus - d, maxMinus + d]


def intersect(rect1, rect2):
    ans = [max(rect1[0], rect2[0]), min(rect1[1], rect2[1]), max(rect1[2], rect2[2]), min(rect1[3], rect2[3])]
    return ans


def get_set(set_xy, tuple_xy, delta):
    x, y = tuple_xy
    for i in range(1, delta + 1):
        set_xy.add((x, y + i))
        set_xy.add((x + i, y))
        set_xy.add((x, y - i))
        set_xy.add((x - i, y))
        for j in range(i):
            set_xy.add((x + j, y + i - j))
            set_xy.add((x + i - j, y - j))
            set_xy.add((x - j, y - i + j))
            set_xy.add((x - i + j, y + j))


# t, d, n = map(int, input().split())

# tuple_prev = tuple()
# tuple_last = (0, 0)

# for i in range(n):
#     x, y = map(int, input().split())
#     tuple_prev = tuple_last
#     tuple_last = (x, y)

# set_prev = {tuple_prev}
# set_last = {tuple_last}
# result = set()

# get_set(set_prev, tuple_prev, t + d)
# get_set(set_last, tuple_last, d)

# set_prev = set_prev.intersection(set_last)

# for item in set_prev:
#     x, y = item
#     if abs(x) + abs(y) <= t * n:
#         result.add((x, y))

# print(len(result))
# for item in sorted(result):
#     print(*item)


while True:
    t = random.randint(1, 100)
    d = random.randint(1, 100)
    n = random.randint(1, 100)

    # t, d, n = map(int, input().split())
    posRect = (0, 0, 0, 0)

    for _ in range(n):
        posRect = extend(posRect, t)
        # navX, navY = map(int, input().split())
        navX = random.randint(-100, 100)
        navY = random.randint(-100, 100)
        navRect = extend((navX + navY, navX + navY, navX - navY, navX - navY), d)
        posRect = intersect(posRect, navRect)
    points = []
    for xPlusY in range(posRect[0], posRect[1] + 1):
        for xMinusY in range(posRect[2], posRect[3] + 1):
            if (xPlusY + xMinusY) % 2 == 0:
                x = (xPlusY + xMinusY) // 2
                y = xPlusY - x
                points.append((x, y))

    # print(len(points))
    # for point in points:
    #     print(*point)оритмы
