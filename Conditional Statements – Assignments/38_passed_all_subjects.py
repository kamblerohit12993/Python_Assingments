# Program 38: Write a program to check whether a student passed all subjects. 

sub1 = int(input("Enter marks for Subject 1: "))
sub2 = int(input("Enter marks for Subject 2: "))
sub3 = int(input("Enter marks for Subject 3: "))

if sub1 >= 35 and sub2 >= 35 and sub3 >= 35:
    print("Student has passed all subjects")
else:
    print("Student has failed")


    