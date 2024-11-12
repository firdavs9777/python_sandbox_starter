# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

class Animal: 
  def __init__(self,name,species):
    self.name = name 
    self.species = species
  def make_sound(self):
    return f"{self.name} makes a sound"
  
class Dog(Animal):
  def __init__(self, name, breed):
    super().__init__(name, "Dog")
    self.breed = breed
  def make_sound(self):
    return f"{self.name} barks!!"  

# Encapsulation and Private Attributes 
class BankAccount: 
  def __init__(self, owner, balance = 0):
    self.owner = owner 
    self.___balance = balance 

  def deposit(self,amount):
    self.___balance += amount
  
  def get_balance(self):
    return self.___balance


# Using class and static methods
class Utility:
    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def info(cls):
        return f"This is the {cls.__name__} class."
    
# Creating instances 
dog = Dog('Buddy',"Golder")
print(dog.make_sound())
    

account = BankAccount("John Doe")
account.deposit(100)
print(account.get_balance())  # Output: 100

# Using class methods
print(Utility.info())