# Program 40: Demonstrate all list methods

numbers = [10, 20, 30, 20, 40]

print("Original List:", numbers)

numbers.append(50)
print("After append():", numbers)

numbers.insert(1, 15)
print("After insert():", numbers)

numbers.remove(20)
print("After remove():", numbers)

numbers.pop()
print("After pop():", numbers)

print("Count of 20:", numbers.count(20))
print("Index of 30:", numbers.index(30))

new_list = numbers.copy()
print("After copy():", new_list)

numbers.sort()
print("After sort():", numbers)

numbers.reverse()
print("After reverse():", numbers)

numbers.extend([60, 70])
print("After extend():", numbers)

numbers.clear()
print("After clear():", numbers)



