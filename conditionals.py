# If/ Else conditions are used to decide to do something based on something being true or false

x = 10
y = 20 


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple If Comparison 
if(x == y):
  print(f'{x} is equal to {y}')

# Simple If Else Comparison 
if(x > y):
  print(f'{x} is bigger than {y}')  
else:
  print(f'{y} is bigger than {x}')

# Elif 
if x > y:
  print(f'{x} is greater than {y}')
elif x == y:
  print('Both equal numbers')
else:
  print(f'{x} is less than {y}')

# Nested If 
if x > 2:
  if x <= 10:
    print(f'{x} is less than 2 and greater than 10')

# Logical operators (and, or, not) - Used to combine conditional statements
# and 

if x > 2 and x <=10:
  print(f'{x} is less than 2 and greater than 10')

# or

if x > 2 or x <=10:
  print(f'{x} is less than 2 and greater than 10')

if not(x == y): 
  print('Both are equals')


# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

# in
my_list = [1, 2, 3, 4]
print(3 in my_list)   # Output: True
print(5 in my_list)    #output False

# not in

my_list = [1, 2, 3, 4]
print(5 not in my_list)  # Output: True
print(3 not in my_list)  # Output: False


sentence = "Python is easy to learn."
print("easy" in sentence)     # Output: True
print("difficult" not in sentence)  # Output: True

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
a = [1,2,3]
b = a 
c = [1,2,3]

# is 
print(a is b)
print(a is c)

# is not
a = [1, 2, 3]
b = [1, 2, 3]
print(a is not b) 