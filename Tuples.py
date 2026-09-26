# Python program about Tuples and frequently used methods/functions

# Tuples are immutable sequences in Python.
# They are useful for fixed collections of values.

# 1. Creating tuples
numbers = (10, 20, 30, 40)
name = ('A', 'B', 'C')
empty_tuple = ()
single_value_tuple = (50,)

print("1. Creating tuples")
print(numbers)
print(name)
print(empty_tuple)
print(single_value_tuple)
print()

# 2. Accessing tuple elements
print("2. Accessing tuple elements")
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("The tuple:", numbers)
print()

# 3. Slicing tuples
print("3. Slicing tuples")
print(numbers[1:4])      # from index 1 to 3
print(numbers[:3])       # first 3 elements
print(numbers[2:])        # from index 2 to end
print()

# 4. Tuple operations
print("4. Tuple operations")
print("Length:", len(numbers))
print("Count of 20:", numbers.count(20))
print("Index of 30:", numbers.index(30))
print("Concatenation:", numbers + (50, 60))
print("Repetition:", (1, 2, 3) * 3)
print()

# 5. Iterating through a tuple
print("5. Iterating through a tuple")
for item in name:
    print(item, end=" ")
print()
print()

# 6. Tuple unpacking
print("6. Tuple unpacking")
a, b, c = name
print("a =", a)
print("b =", b)
print("c =", c)
print()

# 7. Nested tuples
print("7. Nested tuples")
student = ("Alice", (90, 85, 88))
print(student)
print("Student name:", student[0])
print("Marks:", student[1])
print()

# 8. Frequently used functions with tuples
print("8. Frequently used functions")
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))
print("Sorted tuple:", sorted(numbers))
print("Tuple from list:", tuple([1, 2, 3, 4]))
print("List from tuple:", list(numbers))
print()

# 9. Example of tuple immutability
print("9. Tuple immutability")
# numbers[0] = 15  # This will raise TypeError because tuples are immutable
print("Tuples cannot be changed once created.")
print()

# 10. Program output summary
print("10. Summary")
print("Tuples are immutable, ordered, and support many useful operations.")
print("Common tuple methods: count(), index()")
print("Common built-in functions: len(), min(), max(), sum(), sorted(), tuple()")

# End of program
