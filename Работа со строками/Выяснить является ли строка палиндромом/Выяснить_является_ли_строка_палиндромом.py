# -*- coding:1251 -*-
def if_polindrom(line):
    line = line.lower()
    line = line.replace(' ', '')
    return True if line[::-1] == line else False

text = ['Аргентина манит негра',
        'аргентина манит негра',
        'Манит Аргентина негра',
        'мама амам'
        ]

for line in text:
    print(if_polindrom(line))
