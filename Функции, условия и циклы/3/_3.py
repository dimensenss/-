
#-*- coding:cp1251 -*-
#Написать функцию month_to_season(), которая принимает 1 аргумент - номер месяца - и возвращает название сезона, к которому относится этот месяц. 
#Например, передаем 2, на выходе получаем 'Зима'. 

#def month_to_season(i):
#    if (i == 1)or(i == 2) or (i==12):
#        return "Winter"
#    if 3<=i<=5:
#        return "Spring"
#    if 6<=i<=8:
#        return "Summer"
#    if 9<=i<=11:
#        return "Autumn"
#for i in range(1,12):
#    print("i = ",i,month_to_season(i))

def month_to_season(i):
    month_dict ={
        (1,2,12):'Winter',
        (3,4,5):'Spring',
        (6,7,8):'Summer',
        (9,10,11):'Autumn'
    }
    season = None
    for key, value in month_dict.items():
        if i in key:
            season = value
    return season

for i in range(1,12):
    print("i = ",i,month_to_season(i))
