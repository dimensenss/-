
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
