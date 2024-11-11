# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
person = {
  'first_name': 'John',
  'last_name': 'Doe',
  'age': 27
}
# Using a constructor 
person_new = dict(first_name='John', last_name='Doe', age=27)
print(person_new)
#Acessing value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '010-4384-3342'

# Get keys 
print(person.keys())

# Get the values 
print(person.items())

# Make a copy 
person2 = person.copy()
person2['city'] = 'Boston'
print(person2)
print(person)

#Remove item 
del(person['age'])
#Pop method
person.pop('phone')
print(person)
#Clear 
person.clear()
# Get length 
print(len(person2))


# List of dict 
people = [
  {'name':'Davis', 'age':27},
  {'name':'Micheal', 'age':28},
  {'name':'Jordan', 'age':22},
]
print(people)
print(people[0])