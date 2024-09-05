"""
G. Банковские счета
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Некоторый банк хочет внедрить систему управления счетами клиентов, поддерживающую следующие операции:

Пополнение счета клиента.

Снятие денег со счета.

Запрос остатка средств на счете.

Перевод денег между счетами клиентов.

Начисление процентов всем клиентам.

Вам необходимо реализовать такую систему. Клиенты банка идентифицируются именами (уникальная строка, не содержащая
пробелов). Первоначально у банка нет ни одного клиента. Как только для клиента проводится операция пололнения, снятия
или перевода денег, ему заводится счет с нулевым балансом. Все дальнейшие операции проводятся только с этим счетом.
Сумма на счету может быть как положительной, так и отрицательной, при этом всегда является целым числом.

Формат ввода
Входной файл содержит последовательность операций. Возможны следующие операции: DEPOSIT name sum - зачислить сумму sum
на счет клиента name. Если у клиента нет счета, то счет создается. WITHDRAW name sum - снять сумму sum со счета клиента
name. Если у клиента нет счета, то счет создается. BALANCE name - узнать остаток средств на счету клиента name.
TRANSFER name1 name2 sum - перевести сумму sum со счета клиента name1 на счет клиента name2. Если у какого-либо клиента
нет счета, то ему создается счет. INCOME p - начислить всем клиентам, у которых открыты счета, p% от суммы счета.
Проценты начисляются только клиентам с положительным остатком на счету, если у клиента остаток отрицательный, то его
счет не меняется. После начисления процентов сумма на счету остается целой, то есть начисляется только целое число
денежных единиц. Дробная часть начисленных процентов отбрасывается.

Формат вывода
Для каждого запроса BALANCE программа должна вывести остаток на счету данного клиента. Если же у клиента с
запрашиваемым именем не открыт счет в банке, выведите ERROR.
"""

bank = dict()

with open("Trainings 1.0/Lecture 4: “Dictionaries and Counting Sorting”/input.txt", "r", encoding="utf8") as file:
    lines = map(str, file.read().split("\n"))
    for line in lines:
        if line:
            items = line.split()
            operation = items[0]
            if operation == 'DEPOSIT':
                name = items[1]
                sum = int(items[2])
                if name not in bank:
                    bank[name] = 0
                bank[name] += sum
            elif operation == 'WITHDRAW':
                name = items[1]
                sum = int(items[2])
                if name not in bank:
                    bank[name] = 0
                bank[name] -= sum
            elif operation == 'BALANCE':
                name = items[1]
                if name not in bank:
                    print("ERROR")
                else:
                    print(bank[name])
            elif operation == 'TRANSFER':
                name1 = items[1]
                name2 = items[2]
                sum = int(items[3])
                if name1 not in bank:
                    bank[name1] = 0
                if name2 not in bank:
                    bank[name2] = 0
                bank[name1] -= sum
                bank[name2] += sum
            elif operation == 'INCOME':
                percent = int(items[1])
                for key in bank:
                    if bank[key] > 0:
                        bank[key] = int(bank[key] * (1 + percent / 100))
