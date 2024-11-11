# A List is a collection which is ordered and changeable. Allows duplicate members.

#1 Adds an element to the end of the list
fruits = ['apple', 'banana']
fruits.append('cherry')
print(fruits)

#2 Clear all the list items from the list
names = ['John', 'Tomson']
names.clear()
print(names) #Return empty list

##3 Copy the list
cars = ['Ferrari', 'Grandeur','Spark']
new_cars = cars.copy()
print(new_cars)  # return ['Ferrari', 'Grandeur','Spark']

#4 Return the number of times a specific element appears in the list 
foods = ['pasta', 'steak', 'burger', 'pasta']
print(foods.count("pasta")) # return 2

#5 Add all elements of an iterable (list,tuple, set, etc) to the end of the list
drinks = ['coke', 'sprite', 'lemonade']
drinks.extend(['coffee', 'ice-latte'])
print(drinks) # ['coke', 'sprite', 'lemonade','coffee', 'ice-latte' ]

#6 Returns the index of the first occurence of a specific element
indexes = ['index1', 'index2']
print(indexes.index("index2")) # Returns 1

#7 Inserts an element at a specified position in the list
fruits = ["apple", "banana"]
fruits.insert(1, "cherry")
print(fruits)  # Output: ['apple', 'cherry', 'banana']

#8 pop() - Removes and returns the element at the specified index(default is the last item)
pop_items = ['test','test2','test3']
popped_items = pop_items.pop(1) 
print(popped_items) #Output ['test', 'test3']

#9 remove()  - Removes the first occurence of a specific element from the list
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry']

#10 reverse() - Reverses the elements of the list in place
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits) 


#11 sort()
fruits = ["cherry", "banana", "apple"]
fruits.sort()
print(fruits)  # Output: ['apple', 'banana', 'cherry']
#12 sorted()
fruits = ["cherry", "banana", "apple"]
sorted_fruits = sorted(fruits)
print(sorted_fruits)  # Output: ['apple', 'banana', 'cherry']
print(fruits)  # Original list is unchanged: ['cherry', 'banana', 'apple']

#13 len()
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # Output: 3

#14 min()
numbers = [4, 1, 3, 5]
print(min(numbers))  # Output: 1

#15 max()
numbers = [4, 1, 3, 5]
print(max(numbers))  # Output: 5

#16 sum()
numbers = [1, 2, 3, 4]
print(sum(numbers))  # Output: 10

#17 join()
fruits = ["apple", "banana", "cherry"]
print(", ".join(fruits))  # Output: 'apple, banana, cherry'

#18 list()
fruits = list('apple')
print(fruits)
#19 copy()
fruits = ["apple", "banana"]
fruits_copy = fruits.copy()
print(fruits_copy)  # Output: ['apple', 'banana']
