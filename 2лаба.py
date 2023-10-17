import math
x = float(input())
y = float(input())
z = float(input())
a = ((3+math.e**2)/((1+x*x)*abs(y - math.tan(z))))
b = 1+ abs(y-x)+((y-x)**2/2)+((x-y)**2/3)
print(a,b)


a=-2
b=5
c=3
x = 1
while (x <=3):
    y= (b*x+math.pow(a,4))/(c+math.pow(x,3)) +math.pow(x,4)
    x = x+0.2
    print(y)


x = 1
while (x < 3):
    y = abs(math.log(abs(math.cos(x**2)), math.e))/(math.sin(x**2 + math.sqrt(x)))
    print(x, y)
    x = x + 0.1
    

a = int(input())
b = int(input())
c = math.sqrt(math.pow(a,2)+math.pow(b,2))
print(c)

x1 = int(input())
x2 = int(input())
x3 = int(input())
y1 = int(input())
y2 = int(input())
y3 = int(input())
z1 = int(input())
z2 = int(input())
z3 = int(input())
F1 = (x1, y1, z1)
F2 = (x2, y2, z2)
F3 = (x3, y3, z3)

x = x1 + x2 + x3
y = y1 + y2 + y3
z = z1 + z2 + z3

print("Равнодействующая сила F = ({}, {}, {})".format(x, y, z))

a = int(input())
if (a>=1) & (a<=100):
    print( "S = " + str(a*a))
else:
    print("Oshibka")
    exit(0)


A = int(input())
B = int(input())
C = int(input())
if -100 <= (A  or B or C) <=100:
        AC = abs(A-C)
        BC = abs(B-C)
    print( AC,BC, AC+BC)
else:
    print("Oshibka")
    exit(0)
    

prib = float(input())
seb =  float(input())
seb = seb*0.95
rent = (prib/seb) * 100
print(rent)
        

