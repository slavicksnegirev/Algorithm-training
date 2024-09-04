"""
C. Самое частое слово
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Дан текст. Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите то,
которое меньше в лексикографическом порядке.

Формат ввода
Вводится текст.

Формат вывода
Выведите ответ на задачу.
"""

words = {}

with open("Trainings 1.0/Lecture 4: “Dictionaries and Counting Sorting”/input.txt", "r", encoding="utf8") as file:
    s = map(str, file.read().split())
    for word in s:
        if word not in words:
            words[word] = 0
        words[word] += 1
    count_max = -1
    ans = ''
    for word in words:
        if words[word] > count_max:
            count_max = words[word]
            ans = word
        elif words[word] == count_max:
            if word < ans:
                ans = word

    print(ans)
