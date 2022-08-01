def foo(name, **kwargs):
    print(f'Username = {name}')
    """ print(kwargs) """
    for k, v in kwargs.items():
        print(k,':',v)
foo('Ira', age = 17, height = 173, cat_name = 'Michail')    