# Вашей программе на вход подается ссылка на HTML файл.
# Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов,
# на которые есть ссылка.
#
# Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность
# символов, которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть,
# за исключением случаев с относительными ссылками вида
# <a href="../some_path/index.html">.
#
# Сайты следует выводить в алфавитном порядке.
#
# Пример HTML файла:
#
# <a href="http://stepic.org/courses">
# <a href='https://stepic.org'>
# <a href='http://neerc.ifmo.ru:1345'>
# <a href="ftp://mail.ru/distib" >
# <a href="ya.ru">
# <a href="www.ya.ru">
# <a href="../skip_relative_links">
#
# Пример ответа:
#
# mail.ru
# neerc.ifmo.ru
# stepic.org
# www.ya.ru
# ya.ru

# from urllib.parse import urlparse
# o = urlparse("http://xxx.abcdef.com/fdfdf/")
# print(o)
#
# print(o.netloc)

# проходит 1 тест:
import urllib
import lxml.html
import requests
import re
import urllib.request
from urllib.parse import urlparse

url = "https://pastebin.com/raw/7543p0ns"
url = requests.get(url)
html = lxml.html.document_fromstring(url.text)
lst_1 = []
for a in html.iter('a'):
    lst_1.append(a.get('href'))

lst_val = []
for i in lst_1:
    o = urlparse(i)
    if o.netloc:
        lst_val.append(o.netloc)

lllll = sorted(list(set(lst_val)))
for i in lllll:
    print(i)

# верно:


url = input()


def get_links():
    try:
        fp = urllib.request.urlopen(url)
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()
        links = re.findall(r'<a.+href=[\'"]([^./][^\'"]*)[\'"]', mystr)
    except:
        return []
    else:
        return links


def parse_link(link):
    parsed_uri = urlparse(link)
    res = parsed_uri.netloc
    try:
        return res[:res.index(':')]
    except:
        return res
    else:
        return res[:res.index(':')]


links = get_links()

unsorted = list(map(parse_link, links))

for link in sorted(list(set(unsorted))):
    print(link)
