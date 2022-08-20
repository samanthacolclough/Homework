#
# TASK 1
#
# (A)
# Design a parent class called Animal
#
# It must have general attributes: name, date of birth, colour, owner's name
# Also it must have a method that gives you the age of an animal.
#
# For example, if animal's date of birth is 2021/08/21 and today is
# 11 January 2021, the when you call get_age()
# <name your method whatever you want> method, it should give us the age in
# YEAR and MONTH like this: {'years': 0, 'months': 4}
#
# (B)
# B.1
# Design a child class called Dog, which inherits from the Animal class.
# This class should have exactly the same attributes as its parent class,
# as well as additional ones called:
# pet_id and breed (any other attributes are welcome - they are optional).
# You child class Dog should also have a static method called sound(), which
# would give us the sound of the animal ('Grr', 'Bark', whatever you want)
#
# B.2
# Design a child class called Cat, which inherits from the Animal class.
# This class should have exactly the same attributes as its parent class,
# as well as additional ones called:
# pet_id and breed (any other attributes are welcome - they are optional).
# You child class Dog should also have a static method called sound(), which
# would give us the sound of the animal ('Meow', 'Purr', whatever you want)
#
# (C)
# Design an independent class called PetOwner. It is a small class, which should
# have the __init__ method only accepting the 'name of an owner' and 'pet's id'.
#
# SEE THE STARTER CODE BELOW

# you may need to import some packages to manipulate dates
# <your code goes here>
# return {'years': int(year), 'months': int(month)}


from datetime import date, datetime

from datetime import date

class Animal:
    def __init__(self, name, dob, colour, owner):
        self.name = name
        self.dob = {'month': int(), 'year': int ()}
        self.colour = colour
        self.owner = owner

    def get_age(self, dob, age):
        self.dob = {'month': int(), 'year': int ()}
        today = date.today()
        age = today.year - dob.year - ((today.month) < (dob.month))
        return age

    def speak(self):
        print("*silence*")   #if there is no child speak function the animal will return *silence*


b = Animal("sam", {19/2002}, "pink", "tim")
#get_age(b)

# <class Dog with additional attributes: pet_id and breed, sound method HERE>

class Dog(Animal):
    def __init__(self, id, breed, name, dob, colour, owner):
        super().__init__(name, dob, colour, owner)
        self.id = id
        self.breed = breed
        self.name = name
        self.dob = dob
        self.colour = colour
        self.owner = owner

    def speak (self):
        print("woof")

d= Dog(123, "sausage", "Spike", 17/2002, "pink", "Mat")
d.speak()  #---->test to see if dog speaks corrects


# <class Cat with additional attributes: pet_id and breed, sound method HERE>
class Cat(Animal):
    def __init__(self, id, breed, name, dob, colour, owner):
        super().__init__(name, dob, colour, owner)
        self.id = id
        self.breed = breed

    def speak(self):
        print ("Meooooow")

k= Cat(345, "tabby", "Bubbles", 18/1978, "white", "Max")
k.speak()  #K is a variable holding cat data. tested this through function speak, confirmed its a cat


    # <independent class PetOwner with name and pet_id attributes HERE>

class Pet_Owner:
    def __init__(self, name, pet_id):
        self.name = name
        self.pet_id = super(id)


"""
TASK 2

We are going to utilize classes that we created as part of TASK 1. 

Let's imagine that we are a local vet clinic and given the input below, we 
need to add all pets to our register (register is just a dict). 

Please write a function, which parses given input and initializes a class for
each animal, as well as its owner and adds it to the register by id. 

EXAMPLE OUTPUT:

{
 10025: <__main__.Dog object at 0x0829DFB8>,
 10026: <__main__.Cat object at 0x082B4D90>,
 10042: <__main__.Dog object at 0x082B4130>,
 10053: <__main__.Dog object at 0x082B47F0>,
 10058: <__main__.Cat object at 0x07C80B50>
 }

 Each key is a pet id and each value is a newly initialized  Dog or Cat class. 
 Note that within each Dog and Cat class the variable "self.owner" is also 
 a class PetOwner with all relevant attributes.

SEE THE STARTER CODE BELOW

"""
# this is the input for your function

pet_info = [
    {'breed': 'German Shepherd',
     'colour': 'brown',
     'dob': '2021/09/21',
     'pet_id': 10025,
     'name': 'Lola',
     'owner': 'Maria Smith',
     'type': 'dog'},
    {'breed': 'Blue Russian',
     'colour': 'white',
     'dob': '2010/03/06',
     'pet_id': 10058,
     'name': 'Snowy',
     'owner': 'Malcolm Graham',
     'type': 'cat'},
    {'breed': 'Border Collie',
     'colour': 'beige',
     'dob': '2019/11/18',
     'pet_id': 10042,
     'name': 'Bailey',
     'owner': 'Priya Patel',
     'type': 'dog'},
    {'breed': 'Pug',
     'colour': 'black',
     'dob': '2021/10/16',
     'pet_id': 10053,
     'name': 'Ziggy',
     'owner': 'Mohamed Moussa',
     'type': 'dog'},
    {'breed': 'Sphynx',
     'colour': 'white',
     'dob': '2015/08/23',
     'pet_id': 10026,
     'name': 'Coco',
     'owner': 'Jennifer Coley',
     'type': 'cat'}
]


def register_pets(data):
    pets = dict()
    if type == 'cat':
        self.animal.append(Cats)

    # <your code goes HERE>
    # don't forget to:
    # initialize the pet Owner as a class and reassign it to its Key
    # check the type to know which class to use for initialization
    # add a newly created pet (Cat or Dog) to your register by its id

    return pets


print(register_pets(pet_info))

"""
TASK 3

Write a function to sum up the digits of a given number.

EXAMPLE:

num = 78
result = 15

num = 333
result = 9

num = 12345
result = 15
===============================

Using recursion = 25 points
Any non recursive solution = 15 points

===============================

Hints for recursive approach:

1) Get the rightmost digit of the number with help of remainder 
‘%’ operator by dividing it with 10

2) Dividing a number by 10 with help of ‘/’ operator and converting it to int
helps you to 'move or iterate' through a number
"""


def get_sum(n):
    sum = 0
    while (n != 0): #if n has a value do below
        sum = sum + (n % 10)  #This gets most right digit and adds it to sum
        n = n // 10

    return sum

n = 12345
print(get_sum(n))


n = 333
print(get_sum(n))

"""
TASK 4

NON-CODING ASSIGNMENT

*You need to write your answer as a mini essay.* 

Please see the code example below. In this example, one of the SOLID 
principles is violated. 

1) Which SOLID principle is violated?
2) How does this principle work and what is its fundamental meaning?
3) Describe what is happening below and how a user who is running the TEST
 code can be confused?
 
 
The below code violates the LISKOV substitution SOLID principle, this principle is defined by a child class being changed or modified without disrupting the parent class or breaking a program to cause an error.

This is an issue in the below code setting the height also changes the width, this will then impact the code for the parent class and the sunctionality of the code.      
In the code below the user is inheritting from class rectangle and attempting to use these parameters to create a function computing the area of a square. This is ocnfusing for the user as these parameters rely on the variable set in the class rectangle. Should those variables be changed this code does not work.  

"""


class Rectangle:

    def __init__(self):
        self.width = None
        self.height = None

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return self.width * self.height


class Square(Rectangle):

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.height = height
        self.width = height


# TEST  - code run

my_rectangle = Square()

my_rectangle.set_height(5)
my_rectangle.set_width(10)

print(my_rectangle.get_area())

