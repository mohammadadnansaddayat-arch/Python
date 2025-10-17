a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a<b and a<c:
    print("The first number is the smallest: ", a)
elif b<a and b<c:
    print("The second number is the smallest: ", b)
else:
    print("The third nuumber is the smallest.", c)