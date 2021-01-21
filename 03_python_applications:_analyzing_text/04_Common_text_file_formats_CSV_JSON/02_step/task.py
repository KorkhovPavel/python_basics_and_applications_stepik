# Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по на
# стоящее время.
#
# Одним из атрибутов преступления является его тип – Primary Type.
#
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

import csv

lst = []
with open('Crimes.csv', newline='') as File:
    reader = csv.DictReader(File)
    for row in reader:
        if '2015' in row['Date']:
            lst.append(row)
ppp = {}
for i in lst:
    if str(i['Primary Type']) in ppp:
        ppp[str(i['Primary Type'])] += 1
    else:
        ppp[str(i['Primary Type'])] = 1
print(ppp)
