NUM = 30
DIV_NUM = 3

lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20, 1, 44, 67]
sum = 0
for i in lst:
    if (i < NUM and i % DIV_NUM == 0):
        print(i, end =", ")
    else:
        sum += i
        
print("sum = ",sum)

