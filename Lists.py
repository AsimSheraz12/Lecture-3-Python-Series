# Lists in Python
# A list is an ordered, mutable collection of items.

# 1. Creating a list
fruits = ["apple", "banana", "mango", "orange"]
numbers = [10, 20, 30, 40]
mixed = [1, "hello", True, 3.5]

print("Fruits:", fruits)
print("Numbers:", numbers)
print("Mixed:", mixed)

# 2. Accessing list items
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Second to fourth:", fruits[1:4])

# 3. Updating list items
fruits[1] = "blueberry"
print("Updated fruits:", fruits)

# 4. Adding items to a list
fruits.append("grape")
print("After append:", fruits)

fruits.insert(1, "kiwi")
print("After insert:", fruits)

numbers.extend([50, 60, 70])
print("After extend:", numbers)

# 5. Removing items
fruits.remove("orange")
print("After remove:", fruits)

popped_item = fruits.pop()
print("Popped item:", popped_item)
print("After pop:", fruits)

# 6. Useful list methods
print("Length of fruits:", len(fruits))
print("Index of 'apple':", fruits.index("apple"))
print("Count of 'apple':", fruits.count("apple"))

# Sorting and reversing
numbers.sort()
print("Sorted numbers:", numbers)

numbers.reverse()
print("Reversed numbers:", numbers)

# Copying a list
numbers_copy = numbers.copy()
print("Copied list:", numbers_copy)

# Clearing list
numbers.clear()
print("After clear:", numbers)

# 7. List comprehension (shortcut for creating lists)

# 9. Checking membership
print("Is 'banana' in fruits?", "banana" in fruits)

# 10. Joining list items into a string
sentence = " ".join(fruits)
print("Joined sentence:", sentence)

# Example of a list with duplicate values
marks = [85, 90, 85, 78, 90]
print("Marks:", marks)
print("Count of 90:", marks.count(90))

# Summary of frequently used list methods:
# append(), insert(), extend(), remove(), pop(), clear(), sort(), reverse(), copy(), index(), count(), len()
