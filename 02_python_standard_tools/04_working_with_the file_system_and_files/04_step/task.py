# Вам дается текстовый файл, содержащий некоторое количество непустых строк.
# На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.
#
# Пример входного файла:
# ab
# c
# dde
# ff
#
# Пример выходного файла:
# ff
# dde
# c
# ab

with open("r_test.txt.txt") as fr, open("w_test.txt", 'w') as fw:
    lst = []
    for i in fr:
        lst.append(i)
    for l2 in reversed(lst):
        fw.write(l2)
