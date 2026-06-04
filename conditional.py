username = "monusingh"
password = 4747

given_username = input ("Please enter your username: ")
if given_username == username:
    given_password = int(input("Please enter your password: "))
    if given_password == password:
        print ("Successfully signed in ")
    else: 
        print("incorrect password")
else:
    print("invalid username")

