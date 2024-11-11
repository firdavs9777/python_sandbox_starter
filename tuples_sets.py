# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Simple tuple 
fruit_tuple = ('Orange', 'Mango')
print(fruit_tuple)

# Using constructor 
fruit_tuple = ('Orange', 'Mango')
#Get single value 
print(fruit_tuple[1])
# It cannot change the value
fruit_tuple[1] = 'Grape'
# Tuples with one value should have trailing comma 
fruit_tuple_2 = ('Apple',)
print(fruit_tuple_2)
# Get the length of the tuple 
print(len(fruit_tuple_2))


# A Set is a collection which is unordered and unindexed. No duplicate members.

#Create a set
fruit_set = {'Apple', 'Orange'}

# Check if in set
print('Apples' in fruit_set)

# Add to set 
fruit_set.add('Grape')

# Remove to set 
fruit_set.remove('Grape')

# Clear set
fruit_set.clear()
# Delete set 
del fruit_set
print(fruit_set)