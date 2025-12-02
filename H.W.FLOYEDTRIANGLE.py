row = int(input("Enter the number of rows: "))

a = 1

for i in range(row+1):
    for j in range(i):
        print(a, end=" ")
        a = a + 1
    print()