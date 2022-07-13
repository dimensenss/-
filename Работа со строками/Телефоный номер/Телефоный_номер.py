#(123) 456-7890
def create_phone_number(n):
   res = [str(i) for i in n]
   return '('+"".join(res)[:3]+') '+"".join(res)[3:6]+'-'+"".join(res)[6:]
   #return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 2]))
