# ашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
# За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.
#
# Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной операции строка s перейдет в строку "baba",
# после выполнения двух и операций –
# в строку "bbaa", и дальнейшие операции не будут изменять строку s.
#
# Необходимо узнать, после какого минимального количества операций в строке s не останется вхождений строки a.
# Если операций потребуется более 1000,
# выведите Impossible.
#
# Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений
# строки a, или Impossible, если операций
# потребуется более 1000.
#
# Условие задачи было изменено 12.09.2018
# Sample Input 1:
#
# ababa
# a
# b
# Sample Output 1:
#
# 1
# Sample Input 2:
#
# ababa
# b
# a
# Sample Output 2:
#
# 1
# Sample Input 3:
#
# ababa
# c
# c
# Sample Output 3:
#
# 0
# Sample Input 4:
#
# ababac
# c
# c
# Sample Output 4:
#
# Impossible

s, a, b = 'abaaaba', 'aba', 'ab'
lst = [['ababa', 'a', 'b', 1], ['ababa', 'b', 'a', 1], ['ababa', 'c', 'c', 0], ['ababac', 'c', 'c', 'Impossible']]


# s, a, b = (input().split() for _ in range(3))


def func(s, a, b, r):
    print(s, a, b)
    print(r)
    counter = 0
    while True:
        if a in s:
            s = s.replace(a, b)
            counter += 1
            if counter > 100:
                return 'Impossible'
        else:
            return counter


for i in lst:
    print(func(i[0], i[1], i[2], i[3]))
