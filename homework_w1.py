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

    def __init__(self, total_items, total_price, discount):

        self.total_items = {'bread': 2, 'milk': 3, 'cheese':4 }
        #None  {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    def add_item(self):
        pass

    def remove_item(self):
        pass

    def apply_discount(self):
        pass

    def get_total(self, price):
        total += price
        return total

    def show_items(self):
        pass

    def reset_register(self):
        pass


# EXAMPLE code run:

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
        return self.grade

    def get_subjects(self):
        return self.subjects

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



# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subjects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)


