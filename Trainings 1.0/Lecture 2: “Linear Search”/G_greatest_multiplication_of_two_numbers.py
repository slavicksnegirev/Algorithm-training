"""
G. Наибольшее произведение двух чисел
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Дан список, заполненный произвольными целыми числами. Найдите в этом списке два числа, произведение которых
максимально. Выведите эти числа в порядке неубывания.

Список содержит не менее двух элементов. Числа подобраны так, что ответ однозначен.

Решение должно иметь сложность O(n), где n - размер списка.
"""


array = list(map(int, input().split()))

max_1 = array[0]
max_2 = array[1]
min_1 = array[0]
min_2 = array[1]

if len(array) > 2:
    for i in range(len(array)):
        if array[i] > max_1:
            max_2 = max_1
            max_1 = array[i]
        elif array[i] > max_2:
            max_2 = array[i]
        elif array[i] < min_1:
            min_2 = min_1
            min_1 = array[i]
        elif array[i] < min_2:
            min_2 = array[i]

    if max_1 * max_2 > min_1 * min_2:
        print(max_2, max_1)
    else:
        print(min_1, min_2)
else:
    print(min(max_1, max_2), max(max_1, max_2))
