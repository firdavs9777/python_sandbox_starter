# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces


# Create a simple function 
def sayHello():
  print('Hi')

# Calling a function 
sayHello()

# Functions with arguments  
def greet(name):
    print(f"Hello, {name}!")
greet('Davis')
# Function with multiple arguments 
def greet_two(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")
greet_two("John", "Doe")  # Output: Hello, John Doe!

def sum(num1, num2):
   sum = num1 + num2
   return sum

numSum = sum(1,2)
print(numSum)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1,num2: num1 + num2 
print(getSum(9,2))

addOneToNum = lambda num: num + 1 
print(addOneToNum(23))