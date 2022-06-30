# -*- coding:1251 -*-
def if_polindrom(line):
    line.capitalize()

    reversed_line = line[::-1]
    return reversed_line


text = ['Аргентина манит негра',
        'аргентина манит негра',
        'Манит Аргентина негра']

for line in text:
    print(if_polindrom(line))