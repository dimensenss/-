#-*- coding:1251 -*-
#Дано имя файла. Необходимо вывести его расширение.
def extention(name):
    return name.split('.')[1]

#def extention(name):
#    # Находим индекс точки
#    point_pos = filename.find('.')
#    # Возвращаем срез начиная с позиции после точки и до конца имени файла
#    return filename[point_pos + 1:]

FILE = 'folder1/folder2/file.ext'
print(extention(FILE))
