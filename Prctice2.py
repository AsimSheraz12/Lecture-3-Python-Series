palindrome = (55, 9, 1, 8, 5)

palindrome = sorted(palindrome)

print(palindrome)

palindrome1 = palindrome.copy()

print(palindrome1)

# palindrome2 = tuple(palindrome)

palindrome1.reverse()

palindrome = tuple(palindrome) + tuple(palindrome1)

print(palindrome)