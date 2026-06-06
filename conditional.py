username = "monusingh"
password = 4747

given_username = input ("Kindly enter your username: ")
if given_username == username:
    given_password = int(input("Kindly enter your password: "))
    if given_password == password:
        print ("Successfully signed in ")
    else: 
        print("incorrect password")
else:
    print("invalid username")
for i in range(1, 11):
    print(i)
    
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False        
    

