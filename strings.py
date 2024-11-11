# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = "Davis"
age = 27

#Concatenate
print('Hello I am ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position 
greeting = f"Hello, my name is {name} and I am {age} years old."


# String Methods
s = 'test'


# 1. capitalize()
# Capitalizes the first letter of the string and converts all other letters to lowercase.
s = "hello world"
print(s.capitalize())  # Output: Hello world

# 2. casefold()
# Converts all characters in the string to lowercase (more aggressive than `lower()`).
s = "HELLO World"
print(s.casefold())  # Output: hello world

# 3. center(width, fillchar=' ')
# Centers the string within a specified width and fills with the specified character (default is a space).
s = "Python"
print(s.center(10, '*'))  # Output: **Python**

# 4. count(substring, start=0, end=len(string))
# Returns the number of occurrences of a substring in the string.
s = "hello0 world"
print(s.count("o"))  # Output: 2

# 5. encode(encoding='utf-8', errors='strict')
# Encodes the string into a bytes object using the specified encoding.
s = "hello"
print(s.encode())  # Output: b'hello'

# 6. endswith(suffix, start=0, end=len(string))
# Checks if the string ends with the specified suffix.
s = "hello world"
print(s.endswith("world"))  # Output: True

# 7. expandtabs(tabsize=8)
# Replaces all tab characters (`\t`) in the string with spaces, and the number of spaces is determined by `tabsize`.
s = "hello\tworld"
print(s.expandtabs(4))  # Output: hello   world

# 8. find(substring, start=0, end=len(string))
# Returns the lowest index where the substring is found, or -1 if not found.
s = "hello world"
print(s.find("world"))  # Output: 6

# 9. format(*args, **kwargs)
# Formats the string with arguments, replacing placeholders.
s = "Hello, {}!"
print(s.format("Alice"))  # Output: Hello, Alice!

# 10. index(substring, start=0, end=len(string))
# Similar to `find()`, but raises a `ValueError` if the substring is not found.
s = "hello world"
print(s.index("world"))  # Output: 6

# 11. isalnum()
# Returns `True` if all characters in the string are alphanumeric (letters and numbers).
s = "Hello123"
print(s.isalnum())  # Output: True

# 12. isalpha()
# Returns `True` if all characters in the string are alphabetic.
s = "Hello"
print(s.isalpha())  # Output: True

# 13. isascii()
# Returns `True` if all characters in the string are ASCII characters.
s = "hello"
print(s.isascii())  # Output: True

# 14. isdigit()
# Returns `True` if all characters in the string are digits.
s = "12345"
print(s.isdigit())  # Output: True

# 15. isidentifier()
# Returns `True` if the string is a valid Python identifier (variable name).
s = "my_variable"
print(s.isidentifier())  # Output: True

# 16. islower()
# Returns `True` if all characters in the string are lowercase.
s = "hello"
print(s.islower())  # Output: True

# 17. isnumeric()
# Returns `True` if all characters in the string are numeric.
s = "12345"
print(s.isnumeric())  # Output: True

# 18. isprintable()
# Returns `True` if all characters in the string are printable.
s = "hello"
print(s.isprintable())  # Output: True

# 19. isspace()
# Returns `True` if all characters in the string are whitespace.
s = "   "
print(s.isspace())  # Output: True

# 20. istitle()
# Returns `True` if the string is a title (capitalized words).
s = "Hello World"
print(s.istitle())  # Output: True

# 21. isupper()
# Returns `True` if all characters in the string are uppercase.
s = "HELLO"
print(s.isupper())  # Output: True

# 22. join(iterable)
# Joins elements of an iterable (list, tuple, etc.) with the string as a separator.
s = "-"
print(s.join(["apple", "banana", "cherry"]))  # Output: apple-banana-cherry

# 23. ljust(width, fillchar=' ')
# Left-justifies the string, padding it with spaces or the specified character until it reaches the given width.
s = "Hello"
print(s.ljust(10, '*'))  # Output: Hello*****

# 24. lower()
# Converts all characters in the string to lowercase.
s = "HELLO"
print(s.lower())  # Output: hello

# 25. lstrip([chars])
# Removes leading whitespaces or the specified characters from the left side of the string.
s = "   hello"
print(s.lstrip())  # Output: hello

# 26. replace(old, new, count=-1)
# Replaces occurrences of a substring with another substring.
s = "hello world"
print(s.replace("world", "everyone"))  # Output: hello everyone

# 27. rfind(substring, start=0, end=len(string))
# Returns the highest index where the substring is found, or -1 if not found.
s = "hello world"
print(s.rfind("o"))  # Output: 7

# 28. rjust(width, fillchar=' ')
# Right-justifies the string, padding it with spaces or the specified character.
s = "Hello"
print(s.rjust(10, '*'))  # Output: *****Hello

# 29. rstrip([chars])
# Removes trailing whitespaces or the specified characters from the right side of the string.
s = "hello   "
print(s.rstrip())  # Output: hello

# 30. split(sep=None, maxsplit=-1)
# Splits the string into a list at each occurrence of the separator (default is whitespace).
s = "hello world"
print(s.split())  # Output: ['hello', 'world']

# 31. splitlines(keepends=False)
# Splits the string at line breaks (newlines).
s = "Hello\nWorld"
print(s.splitlines())  # Output: ['Hello', 'World']

# 32. swapcase()
# Swaps the case of all characters in the string.
s = "Hello World"
print(s.swapcase())  # Output: hELLO wORLD

# 33. title()
# Capitalizes the first letter of each word in the string.
s = "hello world"
print(s.title())  # Output: Hello World

# 34. upper()
# Converts all characters in the string to uppercase.
s = "hello"
print(s.upper())  # Output: HELLO

# 35. zfill(width)
# Pads the string with zeroes on the left to reach the specified width.
s = "42"
print(s.zfill(5))  # Output: 00042

# 36. partition(separator)
# Splits the string into a tuple containing three parts: the part before the separator, the separator itself, and the part after it.
s = "hello world"
print(s.partition(" "))  # Output: ('hello', ' ', 'world')
