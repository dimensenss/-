import random as r
class Line:
    def __init__(self, a,b,c,d):
        self.sp = a, b
        self.ep = c, d
class Rect:
    def __init__(self, a,b,c,d):
        self.sp = (a, b)
        self.ep = (c, d)
class Ellipse:
    def __init__(self, a,b,c,d):
        self.sp = (a, b)
        self.ep = (c, d)
elements = []
for _ in range(217):
    a = r.randint(0,9)
    b = r.randint(0,9)
    c = r.randint(0,9)
    d = r.randint(0,9)
    elements.append(r.choice([Line(0,0,0,0), Rect(a,b,c,d), Ellipse(a,b,c,d)]))
for i in elements:      
    print(i.__dict__)