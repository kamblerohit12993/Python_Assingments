# Program 20: Write a program to check ticket price based on age.

age = int(input("Enter your age: "))

if age < 5: 
    print("Ticket price is Rs. 0") 
elif age <= 12: 
    print("Ticket price is Rs. 50") 
elif age <= 59: 
    print("Ticket price is Rs. 100") 
else: 
    print("Ticket price is Rs. 60")
