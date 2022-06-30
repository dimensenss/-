def inverse(line):
    lst = line.split(', ')
    lst.reverse()
    return ', '.join(lst)

line = 'football, basketball'
print(inverse(line))


