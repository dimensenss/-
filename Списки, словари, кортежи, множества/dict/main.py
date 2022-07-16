def foo(string):
    """ dictionary = {}
    value =[]
    string = set(text)
    if len(text) == 0: return dictionary
    for i in string:
        count = 0
        for j in text:
            if i == j:
                count +=1
        value.append([i, count])
        dictionary.update(value)   
    return dictionary """
    
    return {i: string.count(i) for i in string}

def main():
    print(foo('aba'))
    
if __name__ == "__main__":
    main()
    