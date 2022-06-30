
dict = {
    1 : 'value_1', 
    2 : 'value_2',
    3 : 'value_3',
        }
dict['stroka'] = 23
dict[('First', 'Second')] = [1,1,1, ('1','2')]
item= dict['stroka']
print(item)
DeletedItem = dict.pop(2)
print(DeletedItem)
print(dict.values())

print("\n\n", dict)
print(dict.get(('First', 'Second')))


