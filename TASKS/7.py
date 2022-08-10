class Point:
    def __init__(self, x, y, color = 'black'):
        self.x = x
        self.y = y
        self.color = color
        
points = []  
p1 = Point(10, 20)
p2 = Point(12, 5, 'red')      
for i in range(1, 2000, 2):
    if i ==3:
        points.append(Point(i, i, 'yellow'))
    else:
        points.append(Point(i,i))
for i in range(1000):    
    print(points[i].__dict__)
print(len(points))                