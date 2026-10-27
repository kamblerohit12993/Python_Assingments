# Program 32: Write a program to check whether a student is eligible for an exam (attendance + marks).

attendance = float(input("Enter your attendance percentage: "))
marks = float(input("Enter your marks: "))

if attendance >= 75:
    if marks >= 40:
        print("The student is eligible for the exam.")
    else:
        print("The student is not eligible for the exam.")

else:
    print("The student is not eligible due to low attendance.")


    