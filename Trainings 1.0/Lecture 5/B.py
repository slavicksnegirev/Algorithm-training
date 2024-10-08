"""
B. Сумма номеров

Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Вася очень любит везде искать своё счастливое число K. Каждый день он ходит в школу по улице, вдоль которой
припарковано N машин. Он заинтересовался вопросом, сколько существует наборов машин, стоящих подряд на местах
с L до R, что сумма их номеров равна K. Помогите Васе узнать ответ на его вопрос.
Например, если число N = 5, K = 17, а номера машин равны 17, 7, 10, 7, 10, то существует 4 набора машин:
17 (L=1,R=1),
7, 10 (L=2,R=3)
10, 7 (L=3,R=4),
7, 10 (L=4,R=5)
Формат ввода

В первой строке входных данных задаются числа N и K (1≤N≤100000, 1≤K≤10^9).
Во второй строке содержится N чисел, задающих номера машин. Номера машин могут принимать значения
от 1 до 999 включительно.
Формат вывода

Необходимо вывести одно число — количество наборов.
"""
N, K = map(int, input().split())
cars = list(map(int, input().split()))

L, R = 0, 0
cur_sum = 0
paar_count = 0

while R < N:
    if cur_sum < K:
        cur_sum += cars[R]
        R += 1
    elif cur_sum > K:
        cur_sum -= cars[L]
        L += 1
    else:
        paar_count += 1
        cur_sum -= cars[L]
        L += 1

while L < N:
    if cur_sum == K:
        paar_count += 1
    cur_sum -= cars[L]
    L += 1

print(paar_count)
