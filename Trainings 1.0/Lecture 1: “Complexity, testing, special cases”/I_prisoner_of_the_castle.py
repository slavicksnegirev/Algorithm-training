"""
I. Узник замка Иф
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
За многие годы заточения узник замка Иф проделал в стене прямоугольное отверстие размером D × E.
Замок Иф сложен из кирпичей, размером A × B × C. Определите, сможет ли узник выбрасывать кирпичи в море через это
отверстие, если стороны кирпича должны быть параллельны сторонам отверстия.

Формат ввода
Программа получает на вход числа A, B, C, D, E.

Формат вывода
Программа должна вывести слово YES или NO.
"""

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

tmp = [A, B, C]

tmp.sort()

if tmp[0] <= min(D, E) and tmp[1] <= max(D, E):
    print("YES")
else:
    print("NO")
