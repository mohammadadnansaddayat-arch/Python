m = int(input("Enter your mark: "))

if m < 33:
    print("grade:F")
elif 33 <= m <= 39:
    print("grade:D")
elif 40 <= m <= 49:
    print("grade:C")
elif 50 <= m <= 59:
    print("grade:B")
elif 60 <= m <= 69:
    print("grade:A-")
elif 70 <= m <= 79:
    print("grade:A")
elif 80 <= m <= 100:
    print("grade:A+")
else:
    print("You have to write a number.")