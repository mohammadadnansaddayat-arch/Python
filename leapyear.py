y = int(input("Enter a year: "))

if y%400 == 0:
    print(y,"The year is a leap year.")
elif y%100 == 0:
    print(y,"The  year is not a leap year.")
elif y%4 == 0:
    print(y,"The year is a leap year.")
else:
    print(y,"The year is not a leap year.")