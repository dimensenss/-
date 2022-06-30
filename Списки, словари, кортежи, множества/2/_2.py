students = {
   'student_1' :{
       'Name' : ('Irina', 'zmievskaya'),
       'Age': 17,
       'Semestr': 3
   },
   'student_2':{
       'Name' : ('Dmytro', 'khOma'),
       'Age': 18,
       'Semestr': 3
   },
   'student_3':{
       'Name' : ('alex', 'Marley'),
       'Age': 18,
       'Semestr': 3
   },
   'student_4':{
       'Name' : ('Olya', 'Sunny'),
       'Age': 18,
       'Semestr': 3
   }
}
print(students.items(),"\n\n")
names = []
for i in students:
    names.append(students[i]['Name'])    
names.sort()

print("Names : ",names,"\n")


#print(students['student_1'])
#print(students['student_2']['Name'][1])