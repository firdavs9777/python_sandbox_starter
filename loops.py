# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

fruits = ['apple', 'banana','cherry']
for fruit in fruits:
  print(fruit)

# For Loop
for i in range(5):
  print(i)

# While loops execute a set of statements as long as a condition is true.
count = 0
while count < 5:
  print(count)
  count += 1

print('BreaK')
# Break Example 
for i in range(10):
    if i == 5:
        break
    print(i)
