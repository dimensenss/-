class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')
    def insert(self, data):
        for i in data:
            self.lst_data.append(dict(zip(self.FIELDS, i.split(' '))))
        return self.lst_data
        
    def select(self, a, b):
        return self.lst_data[a-1: b]
    
lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']        
db = DataBase()
print(db.insert(lst_in))   
print(db.select(1, 2))     