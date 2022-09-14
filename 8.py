x = int(input("a: "))
y = int(input("b: "))
z = int(input("c: "))
if x == y and y == z :
    print("Equilateral triangle")
elif (x==y) or (y==z) or (x==z):
    print("Isosceles triangle")
else:
    print("Scalene triangle")