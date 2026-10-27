#  Multiplication Table and Number Analyzer

number = int(input("Enter a positive number for multiplication table: "))

if number <= 0:
    print("Invalid number! Please enter a positive number.")

else:
    print("\n----- Multiplication Table -----")

    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

    start = int(input("\nEnter starting number of range: "))
    end = int(input("Enter ending number of range: "))

    if start > end:
        print("Invalid range! Starting number must be less than or equal to ending number.")

    else:
        even_count = 0
        odd_count = 0
        total_sum = 0

        for i in range(start, end + 1):
            total_sum = total_sum + i

            if i % 2 == 0:
                even_count = even_count + 1
            else:
                odd_count = odd_count + 1

        print("\n----- Number Analyzer -----")
        print("Starting Number:", start)
        print("Ending Number:", end)
        print("Even Numbers Count:", even_count)
        print("Odd Numbers Count:", odd_count)
        print("Sum of Range:", total_sum)