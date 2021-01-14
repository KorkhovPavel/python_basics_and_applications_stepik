# Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
#
# Выведите одно число – количество вхождений строки t в строку s.
#
# Пример:
# s = "abababa"
# t = "aba"
#
# Вхождения строки t в строку s:
# abababa
# abababa
# abababa
#
# Sample Input 1:
#
# abababa
# aba
# Sample Output 1:
#
# 3
# Sample Input 2:
#
# abababa
# abc
# Sample Output 2:
#
# 0
# Sample Input 3:
#
# abc
# abc
# Sample Output 3:
#
# 1
# Sample Input 4:
#
# aaaaa
# a
# Sample Output 4:
#
# 5
lst = [['abababa', 'aba'], ['abababa', 'abc'], ['abc', 'abc'], ['aaaaa', 'a']]


def func(x, y):
    counter = 0
    pin = True
    while pin:
        num = x.find(y)
        if y in x:
            counter += 1
            x = x[num + 1:]
        else:
            pin = False
    return counter


for i in lst:
    print(func(i[0], i[1]))
