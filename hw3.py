# Homework

#TASK 1
# Q1 Create a program that tells you whether or not you need an umbrella when you leave the house.
weather = (input("is it raining today? yes/ no"))
raining= weather == "yes"
if weather:
  print ("dont forget your umberella!")
else:
  print ("enjoy the sunshine")

#Q2
#There are a few things wrong with this, firstly we are missing the float
# function which tells Python that we will be expecting numbers as a return value.
# Secondly we don’t need the 20+5, this can be shortened. And lastly the wrong >/< symbol was
# being used so the programme was returning the wrong answer.
# I’ve written the correct code below:
my_money = float(input('How much money do you have? '))
boat_cost = 25

if my_money > boat_cost:
	print('You can afford the boat hire')
else :
	print('You cannot afford the board hire')


#Q3
book_year = int(input("what year was the book written?"))
# year_per_cen=
cent = (int(book_year - 1) // 100 + 1)
cen = (int((cent - 1) * 100))
decade = (int(book_year - cen))

if cent ==19:
  century = ("Nineteetnth Century")
else:
  if cent==20:
   century = ("Twentieth Century")

if decade <= 9:
  print ((century), 'first decade')
elif decade >= 10:
  print ((century), 'Teenies')
elif decade >= 20:
  print ((century), 'Twenties')
elif decade >= 30:
  print ((century), 'Thirties')
elif decade >= 40:
  print ((century), 'Forties')
elif decade >= 50:
  print ((century), 'Fithties')
elif decade >= 60:
  print ((century), 'Sixties')
elif decade >= 70:
  print ((century), 'Seventies')
elif decade >= 80:
  print ((century), 'Eighties')
elif decade >= 90:
  print ((century), 'Nineties')


#task 2
#q1

#This programme shows a different answer because of the [1]- this value returns the corresponding value in the list.
# As coding languages will start counting the first item as 0, python does not count ‘oranges;, but instead
# counts ‘cat food’. To change this to start from the beginning of the list, we must start from one. print(shopping_list[0])

#q2
item = {
'white': 1.50,
'milk': 1.20,
'dark': 1.80,
'vegan': 2.00,
}

item = (input("what chocolate would you like to buy?"))
if item =="white":
  print =("you’re total is 1.50")
if item == "milk":
  print =("you’re total is 1.20")
if item == "dark":
  print=("you’re total is 1.80")
if item =="vegan":
  print= ("you’re total is 2.00")

#q3 sorry no clue


#task 3
#q1 Pip is a tool that is used in python to manage packages, pip allows you to install
# and work with packages that aren’t part of the python library.
# For example pip may allow you to use other resources such as MYSQL through downloading
# my sql connector.

#Q2 The problem with those code is that the user has written ‘r’ , this is a read function
# which will only allow the user the read the txt document. Read function does not allow you
# to append or make changes such as the ‘write’ function. For the to work correctly the ‘r’ must
# be replaced with ‘w’

# Q3

# T1

file = open('song.txt', 'r')

print(file)
file = open('song.txt', 'w')
file.write("You could never know what it's like \n")
file.write("Your blood like winter freezes just like ice \n")
file.write("And there's a cold lonely light that shines from you \n")
file.write("You'll wind up like the wreck you hide behind that mask you use \n")
file.write("And did you think this fool could never win?\n")
file.write("Your blood like winter freezes just like ice \n")
file.write("Well look at me, I'm coming back again \n")
file.write("I got a taste of love in a simple way \n")
file.write("And if you need to know while I'm still standing, you just fade away \n")
file.write("Don't you know I'm still standing better than I ever did \n")
file.write("Looking like a true survivor, feeling like a little kid \n")
file.write("I'm still standing after all this time \n")
file.write("Picking up the pieces of my life without you on my mind \n")
file.write("I'm still standing (Yeah, yeah, yeah) \n")
file.write("I'm still standing (Yeah, yeah, yeah) \n")
file.close()

