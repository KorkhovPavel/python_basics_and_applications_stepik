# Вам дана последовательность строк.
# Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).
#
# Sample Input:
#
# blabla is a tandem repetition
# 123123 is good too
# go go
# aaa
# Sample Output:
#
# blabla is a tandem repetition
# 123123 is good too

import sys
import re

pattern = r'human'
for line in sys.stdin:
    res = re.sub(pattern, 'computer',line)
    print(res)