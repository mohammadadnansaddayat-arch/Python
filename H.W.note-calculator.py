n = int(input("Enter the number of note: "))

note = n // 1000
print("1000tk: ",note)
n = n % 1000

note = n // 500
print("500tk: ",note)
n = n % 500

note = n // 200
print("200tk: ", note)
n = n % 200

note = n // 100
print("100tk: ",note)
n = n % 100

note = n // 50
print("50tk: ",note)
n = n % 50

note = n // 20
print("20tk: ",note)
n = n % 20

note = n // 10
print("10tk: ",note)
n = n % 10