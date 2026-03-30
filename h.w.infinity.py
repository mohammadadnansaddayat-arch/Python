running = True

while running:
    n = str(input("Enter a number or enter 'x' to quit: "))
    if n.lower() == "x":
        running = False
        print("exiting the program...")
    else:
        n = int(n)
        if n % 2 == 0:
            print(f"{n,} is odd.")
        else:
            print(f"{n} is even.")