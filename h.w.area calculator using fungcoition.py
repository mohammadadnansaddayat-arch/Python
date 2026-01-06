def squareArea(side):
    area = side ** 2
    return area

def rectangleArea(length,width):
    area = length * width
    return area

def circleArea(radius):
    area = 3.14159 * radius ** 2
    return area

def triangleArea(base,height):
    area = (base * height)
    return area

print(">>>>>>>>>>>> AREA CALCULATOR<<<<<<<<<<<<<<")
print("Choose a shape to calculate the AREA:")
print("1.square")
print("2.rectangle")
print("3.circle")
print("4.triangle")

chooice = int(input("your chooice: "))

if chooice == 1:
    side = float(input("Enter the side length of the square: "))
    area = squareArea(side)
    print(f"The area of the square is: {area:.2f}")

elif chooice == 2:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = rectangleArea(length,width)
    print(f"The area of the rectangle is: {area:.2f}")

elif chooice == 3:
    radius = float(input("Enter the radius of the circle: "))
    area = circleArea(radius)
    print(f"The area of the circle is: {area:.2f}")

elif chooice == 4:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = triangleArea(base,height)
    print(f"The area of the circle is: {area:.2f}")

else:
    print("Invaild Input")