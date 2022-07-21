"""

TASK 1

Write a class to represent a Cash Register.
Your class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""


class CashRegister:

    def __init__(self, discount=0):

        self.total_items = dict() #None  {'item': 'price'}
        self.total_price = 0
        self.discount = discount

    def add_item(self, item, price):
        self.items = self.items.append(item.price) #This adds an item
        self.total_items = self.items.append(item) #This adds item to total price

    def remove_item(self, item, price):
        self.items= self.items.pop(itemprice)
        self.total_items = self.items.pop(item) #This removes an item from total price
        return ("You have removed an item from your basket")

    def apply_discount(self): #This discounts deducts 10% when you spend 50 or over
        discount= self.total_price / 10
        if self.total_price >= 50:
            price= self.total_price -( self.total_price/ self.discount)
            return price

        else:
            return "Discount is not eligible, please spend £50 or over to receive 10% off "


    def get_total(self, price):
        return "Hello, your total for today is", self.total_price

    def show_items(self):
        return total_items

    def get_receipt(self, items, price):
        return total_items, total_price


    def reset_register(self):
        self.total_price =[]
        self.items= []
        return "Cash register has been cleared"





#kjbuobljbnln EXAMPLE code run:

# ADD


"""

TASK 2

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 

"""


class Student:

    def __init__(self, name, age, id, grade):
        self.name = name
        self.age = age
        self.id = id
        self.grade= grade # 0-100
        self.subjects = dict()

    def get_grade(self):
        return self.grade #gets students grade

    def get_subjects(self):
        return list (self.subjects) #returns students subjects


class CFG_student(Student):
    def __init__(self, stream, average_grade):
        self.stream= stream
        self.average_grade= average_grade

    def add_subject(self, subject):
        self.subjects.append(subject)

    def remove_subject(self, subject):
        self.subjects.pop(subject)

    def get_subjects(self):
        return list(self.subjects)


class course:
    def __init__(self, name, max_students):
        self.name= name
        self.max_students = max_students
        self.students = []


    def add_student(self, student):   #This method allows us to add new students to a course
        if len(self.students) < self.max_students: #Function only allows a certain number of students to join course
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        pass

s1= Student ("Sarah", 25, 9875, 83)
s2= Student ("Melanie", 33, 5678, 95)
s3= Student ("Pia", 29, 8762, 75)

course= course ("Software", 2) # max students in software is 2
course.add_student(s1)
course.add_student (s2) #Students 1 and 2 added to software stream

#TO BE CONTINUED

# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subjects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)


