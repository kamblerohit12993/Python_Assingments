# Program 24: Write a program to check exam results (Distinction, First Class, Pass, Fail).

marks = float(input("Enter your marks: "))

if marks >= 75:
    print("Result: Distinction")
elif marks >= 60:
    print("Result: First Class")
elif marks >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")


    