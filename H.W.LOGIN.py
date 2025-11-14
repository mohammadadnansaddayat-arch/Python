print("Login System.")
username = input("Enter your username: ")

if username == "username":
    password = input("Enter your password: ")
    if password == "password":
        print("Login susccessfully!")
    else:
        print("Incorrect password!Try again.")
else:
    print("User not found")