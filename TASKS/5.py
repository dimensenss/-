d = {}
class Translator:
    def add(self, eng, rus):
        if eng not in d:
            d[eng] = []
        d[eng].append(rus)
    def remove(self, eng):
        d.pop(eng)
    def translate(self, eng):
        return d[eng]        
    
tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove('car')
print(*tr.translate('go'))
print(d.items())       