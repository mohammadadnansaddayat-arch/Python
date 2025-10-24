cause = str(input("Do you have a medical cause? (YES/NO): ")).lower()

if cause == "yes":
    percentage = int(input("Enter your atenddens percentage: "))
    if percentage >= 60:
        print("You are eligible for exam!")
    else:
        print("You are not eligible for exam!")

if cause == "no":
    percentage = int(input("Enter your atenddens percentage: "))
    if percentage >= 75:
        print("You are eligible for exam!!!!!!!!")
    else:
        print("You are not eligible for exam!!")

else:
    print("INVAILD INPUT!!!")