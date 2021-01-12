# Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.
#
# Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, в которых есть
# хотя
# бы один файл с расширением ".py".
#
# Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом
# порядке.
#
# Для лучшего понимания формата задачи, ознакомьтесь с примером.
# Пример архива
# Пример ответа
import os


def lst_res(dirs):
    res_list = []
    for current_dir, dirs, files in os.walk(dirs):
        # print(current_dir)
        # print(dirs)
        # print(files)
        if '.py' in str(files):
            res_list.append(current_dir)
    return sorted(res_list)


def files_res(res):
    with open('cur.txt','w') as ff:
        for i in res:
            ff.write(f'{i}\n')

# print(lst_res(dirs='main'))
files_res(lst_res(dirs='main'))