# В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
# Во второй строке дано одно число days -- число дней.
#
# Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней,
# равное days.
#
# Примечание:
# Для решения этой задачи используйте стандартный модуль datetime.
# Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta для прибавления дней к дате.
#
# Sample Input 1:
#
# 2016 4 20
# 14
# Sample Output 1:
#
# 2016 5 4
# Sample Input 2:
#
# 2016 2 20
# 9
# Sample Output 2:
#
# 2016 2 29
# Sample Input 3:
#
# 2015 12 31
# 1
# Sample Output 3:
#
# 2016 1 1


import datetime

val1 = list(map(int, input().split()))
val2 = int(input())

val_data = datetime.date(val1[0], val1[1], val1[2])
val_data_plus = val_data + datetime.timedelta(days=val2)
print(val_data_plus.year, val_data_plus.month, val_data_plus.day)
