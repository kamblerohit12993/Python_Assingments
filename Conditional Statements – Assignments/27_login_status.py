# Program 27: Write a program to check login status based on username and password.

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "admin123":
    print("Login successful!")
else:
    print("Invalid username or password. Please try again.")


