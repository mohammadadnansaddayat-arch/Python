students = {
    "101": {"name":"Ahsan","age":"20","grade":"10"},
    "102": {"name":"Rabeya","age":"19","grade":"9"},
    "103": {"name":"ayat","age":"10","grade":"4"}
}

print("orgingal Dictionary")
print(students)

print("\nAcsses student 101:", students["101"])
print("get with .get():", students["102"])

students["104"] = {"name":"Aphra","age":"9","grade":"2"}
print("\nAfter adding new student: ")
print(students)

students["103"]["age"] = 12
print("\nAfter changed 103's age:")
print(students)