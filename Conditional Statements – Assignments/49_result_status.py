# Program 49: Write a program to print result status using match case. 

result = input("Enter result status (pass/fail): ").lower()

match result:
    case "pass":
        print("Congratulations! You have passed.")
    case "fail":
        print("Sorry! You have failed.")
    case _:
        print("Invalid result status")



        