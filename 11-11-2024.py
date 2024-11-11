# Polymorphism:- It refers to the use of a single type entity (method, operator or object) 
#                to represent different types in different scenarios.

# Method overloding:- Two or more methods have the same name but different numbers of parameters or different types of parameters.

#method overriding:-  when you have two methods with the same name that each perform different tasks

# Ex:-
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")     
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747")    

for x in (car1, boat1, plane1):
  x.move()
