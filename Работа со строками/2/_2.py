# -*- coding:1251 -*-
#1. Создайте данную строку
#2. Получите ее длину
#3. Проведите операцию сложения со строкой ‘!’
#4. Проверьте, входит ли подстрока ‘el’ в заданную строку
#5. Посчитайте количество вхождений подстроки ‘ре’
#6. Получите предпоследний символ строки
#7. Получите все символы с нечетными индексами
#8. Определите, сколько слов в строке

line = 'hello world, i am aLive!'

print("Len = ", len(line))
print(line + '!')
print('el' in line)
print('"l" in line =',line.count('l'))
print('last el in line >',line[-1])
print(line[::2])
print('words count = ',line.count(' ')+1)
line = line.split(" ")
for i in range(len(line)):
    line[i] = line[i].capitalize()
line = " ".join(line)
print(line)
