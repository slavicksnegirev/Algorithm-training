"""
A. Возрастает ли список?
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Дан список. Определите, является ли он монотонно возрастающим(то есть верно ли,
что каждый элемент этого списка больше предыдущего).

Выведите YES, если массив монотонно возрастает и NO в противном случае.
"""

sequence = list(map(int, input().split(" ")))


def isIncreases(seq):
    if len(seq) > 1:
        for i in range(len(seq) - 1):
            if seq[i] >= seq[i + 1]:
                return "NO"
    else:
        return "YES"
    return "YES"


print(isIncreases(sequence))

# a = map(int, input().split())
# a = list(a)
# b = a

# print(b, sorted(a))
# if b == sorted(a) and len(set(b)) == len(a):
#     print("YES")
# else:
#     print("NO")
