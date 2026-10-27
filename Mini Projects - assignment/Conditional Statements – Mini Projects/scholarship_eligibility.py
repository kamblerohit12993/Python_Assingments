# Student Scholarship Eligibility

student_name = input("Enter student name: ")
percentage = float(input("Enter percentage: "))
family_income = float(input("Enter annual family income: "))
attendance = float(input("Enter attendance percentage: "))

if percentage < 0 or percentage > 100:
    print("Invalid percentage!")

elif family_income < 0:
    print("Invalid family income!")

elif attendance < 0 or attendance > 100:
    print("Invalid attendance percentage!")

elif percentage >= 75 and family_income <= 400000 and attendance >= 75:

    print("\n----- Scholarship Details -----")
    print("Student Name:", student_name)
    print("Eligibility Status: Eligible")

    if percentage >= 90:
        print("Scholarship Category: Full Scholarship")
    else:
        print("Scholarship Category: Partial Scholarship")

else:
    print("\n----- Scholarship Details -----")
    print("Student Name:", student_name)
    print("Eligibility Status: Not Eligible")
    print("Reason: Basic scholarship conditions are not satisfied.")



