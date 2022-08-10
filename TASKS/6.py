lst_1 = [1,2,3]
lst_2 = ['one', 'two', 'three']
lst = []
d = dict(zip(lst_1, lst_2))
for i in d.items():
    lst.append(i)
print(lst)    