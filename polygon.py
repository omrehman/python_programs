import math
def main():
	print "Please enter the type of n-gon. Ex: for hexagon, put 8 because it has 8 sides."
	n = input("> ")
	print "Please enter the base length for the regular polygon."
	b = input("> ")
	b2 = b-2
	return b,n,b2

#Algorithm

(b,n,b2)= main()
print("n="),n," b=",b," b2=",b2
print("Process: \n")
a = 180*(n-2)/n
print('Angle Degrees on every angle:' ), a
a1 = a/2
print('Angle degrees for half of an angle to us in triangle: '), a1
trig = math.tan(a1)*b2
print('Height: '), trig
areaofTriangle = trig*b/2
print('Area of one triangle(Equilateral): '), areaofTriangle
area = areaofTriangle*n
    
print('\nThe area of your polygon is: '), area

