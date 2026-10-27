# Student Marks and Grade Report

students = int(input("Enter number of students: "))

if students <= 0:
    print("Invalid number of students!")

else:
    total_marks = 0
    pass_count = 0
    fail_count = 0

    for i in range(1, students + 1):
        print("\nStudent", i)

        name = input("Enter student name: ")
        marks = float(input("Enter marks out of 100: "))

        if marks < 0 or marks > 100:
            print("Invalid marks! Enter marks between 0 and 100.")
            continue

        total_marks = total_marks + marks

        if marks >= 75:
            grade = "A"
        elif marks >= 60:
            grade = "B"
        elif marks >= 50:
            grade = "C"
        elif marks >= 40:
            grade = "D"
        else:
            grade = "Fail"

        print("Student Name:", name)
        print("Marks:", marks)
        print("Grade:", grade)

        if marks >= 40:
            pass_count = pass_count + 1
        else:
            fail_count = fail_count + 1

    valid_students = pass_count + fail_count

    print("\n----- Class Report -----")
    print("Total Students:", students)
    print("Valid Student Records:", valid_students)
    print("Passed Students:", pass_count)
    print("Failed Students:", fail_count)

    if valid_students > 0:
        average = total_marks / valid_students
        print("Class Average:", round(average, 2))
    else:
        print("No valid marks entered.")