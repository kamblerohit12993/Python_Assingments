# Program 40: Write a program to check whether a password is valid using nested if.
 

password = input("Enter your password: ")

if len(password) >= 8:
    if password == "Python123":
        print("Valid password")
    else:
        print("Incorrect password")
else:
    print("Password must contain at least 8 characters")



    