# Program 34: Find common elements between two lists

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common = []

for item in list1:
    if item in list2:
        common.append(item)

print("First List:", list1)
print("Second List:", list2)
print("Common Elements:", common)



