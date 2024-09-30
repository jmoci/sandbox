min_length = 3
password_input = input("Password: ")
while len(password_input) < min_length:
    password_input = input(f"Password does not meet minimum length of {min_length}, please try again: ")
for i in range(len(password_input)):
    print("*",sep="",end="")
print()