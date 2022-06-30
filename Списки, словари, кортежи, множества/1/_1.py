list = []
length = int(input("Enter length of list: "))

for el in range(length):
    list.append(++el)

print("\nFirst el in list",list[0],"\nLast el ib list", list[-1])
list.reverse()
print("\nReverse list",list)
list.sort()
print("\nSort list",list)
