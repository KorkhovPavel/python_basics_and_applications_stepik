# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
#
# Примечание:
# Считать все строки по одной из стандартного потока ввода вы можете, например, так
#
# import sys
#
# for line in sys.stdin:
#     line = line.rstrip()
#     # process line
#
# Sample Input:
#
# catcat
# cat and cat
# catac
# cat
# ccaatt
# Sample Output:
#
# catcat
# cat and cat

# def count_overlapping_substrings(haystack, needle):
#     count = 0
#     i = -1
#     while True:
#         i = haystack.find(needle, i+1)
#         if i == -1:
#             return count
#         count += 1
#
# print(count_overlapping_substrings('avavrewwevavavewrewrew vavvavav ', 'vav'))
# -> 6
x = 'Mary had a little lamb'
y = 'ha'
if x.count(y) >= 2:
    print(x)
