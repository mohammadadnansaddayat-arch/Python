marks = (10,20,30,40,50)
fruits = ("mango","apple","banna","cherry","apple")

print("1. Accessing an eliment: ", marks[2])
print("2. Slicing: ", marks[1:4])
print("3. length: ", len(fruits))
print("4. count: ", fruits.count("apple"))
print("5. index: ", fruits.index("banna"))
t3 = marks + fruits
print("6. Concatenation: ", t3)
t4 = marks * 2
print("7. repetion: ", t4)
print("8. membership check: ", 30 in marks)
lst = list(marks)
print("Tuple to list: ", lst)