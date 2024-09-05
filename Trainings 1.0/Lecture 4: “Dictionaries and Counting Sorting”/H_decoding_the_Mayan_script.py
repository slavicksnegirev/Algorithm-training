"""
H. Расшифровка письменности Майя
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Расшифровка письменности Майя оказалась более сложной задачей, чем предполагалось ранними исследованиями. На протяжении
более чем двух сотен лет удалось узнать не так уж много. Основные результаты были получены за последние 30 лет.

Письменность Майя основывается на маленьких рисунках, известных как значки, которые обозначают звуки. Слова языка Майя
обычно записываются с помощью этих значков, которые располагаются рядом друг с другом в некотором порядке.

Одна из проблем расшифровки письменности Майя заключается в определении этого порядка. Рисуя значки некоторого слова,
писатели Майя иногда выбирали позиции для значков, исходя скорее из эстетических взглядов, а не определенных правил.
Это привело к тому, что, хотя звуки для многих значков известны, археологи не всегда уверены, как должно произноситься
записанное слово.

Археологи ищут некоторое слово W. Они знают значки для него, но не знают все возможные способы их расположения.
Поскольку они знают, что Вы приедете на IOI ’06, они просят Вас о помощи. Они дадут Вам g значков, составляющих слово
W, и последовательность S всех значков в надписи, которую они изучают, в порядке их появления. Помогите им, подсчитав
количество возможных появлений слова W.

Задание Напишите программу, которая по значкам слова W и по последовательности S значков надписи подсчитывает
количество всех возможных вхождений слова W в S, то есть количество всех различных позиций идущих подряд g значков в
последовательности S, которые являются какой-либо перестановкой значков слова W .

Формат ввода
1 ≤ g ≤ 3 000, g – количество значков в слове W

g ≤ |S| ≤ 3 000 000 где |S| – количество значков в последовательности S

На вход программы поступают данные в следующем формате:

СТРОКА 1: Содержит два числа, разделенных пробелом – g и |S|. СТРОКА 2: Содержит g последовательных символов, с
помощью которых записывается слово W . Допустимы символы: ‘a’-‘z’ и ‘A’-‘Z’; большие и маленькие буквы считаются
различными. СТРОКА 3: Содержит |S| последовательных символов, которые представляют значки в надписи. Допустимы
символы: ‘a’-‘z’ и ‘A’-‘Z’; большие и маленькие буквы считаются различными.

Формат вывода
Единственная строка выходных данных программы должна содержать количество возможных вхождений слова W в S.
"""
# TODO Time-Limit 
# import random
# import string


# def set_items(keys, d):
#     for key in keys:
#         if key not in d:
#             d[key] = 0
#         d[key] += 1

# # g, s = map(int, input().split())
# # word = input()
# # seq = input()


# def solve1(word, seq, g, s):
#     count = 0
#     script = dict()
#     buffer = dict()

#     set_items(word, script)

#     for i in range(0, s):
#         if seq[i] in script:
#             if seq[i] not in buffer:
#                 buffer.update({seq[i]: 1})
#             else:
#                 buffer[seq[i]] += 1
#             if buffer.items() == script.items():
#                 count += 1
#                 if buffer[seq[i - g + 1]] > 1:
#                     buffer[seq[i - g + 1]] -= 1
#                 else:
#                     buffer.pop(seq[i - g + 1])
#         else:
#             if buffer:
#                 buffer.clear()

#     return count


# def solve2(word, seq, g, s):
#     count = 0
#     script = dict()
#     buffer = dict()

#     set_items(word, script)
#     set_items(seq[:g], buffer)

#     if script.items() == buffer.items():
#         count += 1

#     for i in range(g, s):
#         if buffer[seq[i - g]] > 1:
#             buffer[seq[i - g]] -= 1
#         else:
#             buffer.pop(seq[i - g])
#         if seq[i] not in buffer:
#             buffer.update({seq[i]: 1})
#         else:
#             buffer[seq[i]] += 1
#         if script.items() == buffer.items():
#             count += 1

#     return count


# iteration = 1
# while True:
#     print(iteration)

#     g = random.randint(1, 4)
#     s = random.randint(g, 10)

#     word = ''.join(random.choices(string.ascii_letters, k=g))
#     seq = ''.join(random.choices(string.ascii_letters, k=s))

#     if solve1(word, seq, g, s) != solve2(word, seq, g, s):
#         print(g, s)
#         print(word)
#         print(seq)
#         break

#     iteration += 1

def set_items(keys, d):
    for key in keys:
        if key not in d:
            d[key] = 0
        d[key] += 1


g, s = map(int, input().split())
word = input()
seq = input()

count = 0
script = dict()
buffer = dict()

set_items(word, script)

for i in range(0, s):
    if seq[i] in script:
        if seq[i] not in buffer:
            buffer.update({seq[i]: 1})
        else:
            buffer[seq[i]] += 1
        if sum(buffer.values()) == g:
            if buffer.items() == script.items():
                count += 1
            if buffer[seq[i - g + 1]] > 1:
                buffer[seq[i - g + 1]] -= 1
            else:
                buffer.pop(seq[i - g + 1])
    else:
        if buffer:
            buffer.clear()

print(count)
