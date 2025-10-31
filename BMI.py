w = float(input("Enter your weight in KG: "))
h = float(input("Enter your height in meter: "))

bmi = w / h **2

print("Your BMI is: ", round(bmi,2))

if bmi < 18.5:
    print("YOU ARE UNDER WIEGHT.PLEASE GAIN SOME WEIGTH.")
elif 18.5 <= bmi <=24.9:
    print("YOU ARE IN NORMAL WIEGHT.KEEP IT UP!")
elif 25 <= bmi <= 29.9:
    print("YOU ARE OVERWEIGHT.PLEASE LOSS SOME WEIGHT.")
elif 30 <= bmi <= 39.9:
    print("YOUR ARE OBESE.LOSSING WEIGHT IS EMERGENCY.")
else:
    print("YOU ARE EXTREMLY OBESE.PLEASE GO TO THE DOCTOR AS SOON AS POSSIBLE!!")