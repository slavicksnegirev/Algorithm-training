"""
F. Симметричная последовательность
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Последовательность чисел назовем симметричной, если она одинаково читается как слева направо, так и справа налево.
Например, следующие последовательности являются симметричными:

1 2 3 4 5 4 3 2 1

1 2 1 2 2 1 2 1

Вашей программе будет дана последовательность чисел. Требуется определить, какое минимальное количество и каких чисел
надо приписать в конец этой последовательности, чтобы она стала симметричной.

Формат ввода
Сначала вводится число N — количество элементов исходной последовательности (1 ≤ N ≤ 100). Далее идут N чисел —
элементы этой последовательности, натуральные числа от 1 до 9.

Формат вывода
Выведите сначала число M — минимальное количество элементов, которое надо дописать к последовательности, а потом M
чисел (каждое — от 1 до 9) — числа, которые надо дописать к последовательности.
"""


def sym_sequence(N, array):
    second_array = []
    count = 0

    for i in range(N):
        if array[i] != array[N - 1 - i + count]:
            count = i + 1
            second_array.clear()
            for j in range(count):
                second_array.insert(j, array[j])

    return count, second_array


N = int(input())
array = list(map(int, input().split()))

count, secod_array = sym_sequence(N, array)
secod_array.reverse()
print(count, ' '.join(map(str, secod_array)) if secod_array else "", sep="\n")
