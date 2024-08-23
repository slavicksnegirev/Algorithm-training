"""
B. Определить вид последовательности
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
По последовательности чисел во входных данных определите ее вид:

CONSTANT – последовательность состоит из одинаковых значений
ASCENDING – последовательность является строго возрастающей
WEAKLY ASCENDING – последовательность является нестрого возрастающей
DESCENDING – последовательность является строго убывающей
WEAKLY DESCENDING – последовательность является нестрого убывающей
RANDOM – последовательность не принадлежит ни к одному из вышеупомянутых типов
Формат ввода
По одному на строке поступают числа последовательности ai, |ai| ≤ 109.

Признаком окончания последовательности является число -2× 109. Оно в последовательность не входит.

Формат вывода
В единственной строке выведите тип последовательности.
"""

isConstant = True
isAscendig = True
isDescending = True
isWeak = False

prev_number = int(input())
if prev_number == -2000000000:
    pass
cur_number = int(input())

while cur_number != -2000000000:
    isConstant &= cur_number == prev_number
    isWeak |= cur_number == prev_number
    isAscendig &= cur_number >= prev_number
    isDescending &= cur_number <= prev_number

    prev_number = cur_number
    cur_number = int(input())

if isConstant:
    print("CONSTANT")
elif isAscendig:
    print("WEAKLY ASCENDING" if isWeak else "ASCENDING")
elif isDescending:
    print("WEAKLY DESCENDING" if isWeak else "DESCENDING")
else:
    print("RANDOM")
