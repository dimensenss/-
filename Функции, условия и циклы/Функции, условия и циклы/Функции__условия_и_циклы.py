
data = {3,4,4,4,3,2,True, '33'}
new_frozenset = frozenset([1,3,4,4,4,3,2,True, '334'])
union = data | new_frozenset
intersection = data&new_frozenset

nums = [1,7,7,7,7,6,4,3,2,2]
print(nums)
nums = set(nums)
print(nums)
print(data)
print(new_frozenset)
print(union)
print(intersection)


