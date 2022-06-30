#-*- coding:1251 -*-
def extention(name):
    return name.split('.')[1]

#def extention(name):
#    point_pos = filename.find('.')
#    return filename[point_pos + 1:]

FILE = 'folder1/folder2/file.ext'
print(extention(FILE))
