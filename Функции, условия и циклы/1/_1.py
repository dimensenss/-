# -*- coding: cp1251 -*-
#Напишите программу, которая будет выводить нечетные числа из списка и остановится, если встретит число 139

nums = [1,2,3,4,5,6,7,139,8,9]
odd_nums = []
for i in nums:
    if i % 2 != 0:
        odd_nums.append(i)
    if i is 139:
        break
        
print(nums)
print(odd_nums)
