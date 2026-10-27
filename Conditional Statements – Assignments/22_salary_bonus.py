# Program 22: Write a program to check salary bonus based on years of service.

salary = float(input("Enter your salary: ")) 
years = int(input("Enter years of service: ")) 

if years >= 5: 
    bonus = salary * 0.10 
    print("Bonus amount is:", bonus) 
else: 
    print("No bonus") 

    