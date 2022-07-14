def num_sum(num):
    lst = list(str(num))
    s = 0
    for i in lst:
        s += int(i)
    return s


def num_suma(num):
    lst = [int(item) for item in str(num)]
    return sum(lst)


print(num_sum(32345))
print(num_suma(123456))