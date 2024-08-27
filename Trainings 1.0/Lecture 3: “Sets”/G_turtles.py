"""
G. Черепахи
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Широко известна следующая задача для младших школьников. Три черепахи ползут по дороге. Одна черепаха говорит:
“Впереди меня две черепахи”. Другая черепаха говорит: “Позади меня две черепахи”. Третья черепаха говорит:
“Впереди меня две черепахи и позади меня две черепахи”. Как такое может быть? Ответ: третья черепаха врет!
По дороге одна за другой движутся N черепах. Каждая черепаха говорит фразу вида: “Впереди меня ai черепах,
а позади меня bi черепах”. Ваша задача определить, сколько самое большее количество черепах могут говорить правду.

Формат ввода
В первой строке вводится целое число N (1 ≤ N ≤ 10000) строк, содержащих целые числа ai и bi, по модулю
не превосходящие 10000, описывающие высказывание i-ой черепахи.

Формат вывода
Выведите целое число M – максимальное количество черепах, которые могут говорить правду.
"""

N = int(input())
M = 0

set_a = set()
set_b = set()

for i in range(N):
    a, b = map(int, input().split())
    if a + b == N - 1 and a >= 0 and b >= 0:
        set_a.add(a)
        set_b.add(b)

print(len(set_a))
