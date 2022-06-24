

"""
customer ={
  'pin': 1234,
  'balance': 100
  }

try:
  Pin != customer['pin']
except Exception:
  attempts = 3
  Pin= int (input ("Sorry, incorrect pin. You have {} remaining attempts. Please enter the correct pin: ".format(attempts)))
"""
Pin = float (input("Enter your pin number:"))
End = ("Thank you, Goodbye.")

correct_pin= Pin == 1234
balance = 100

if Pin != "1234":
  print ("ERROR: incorrect pin")
  attempts =3
  int(input("Sorry, incorrect pin. You have {} remaining attempts. Please enter the correct pin: ".format(attempts)))





def withdraw():
  if True:
    amount = float(input("How much money would you like to withdraw? Please enter the amount"))
    if amount > balance:
      print("You have insufficient funds in your bank account. Please deposit more money to make this request.")
      print(End)
    else:
      new_balance = balance - amount
      confirm= input(
        f"You have selected {amount} GBP. This money will be withdrawn from your available funds. Your remianing balance is {new_balance}. Confirm yes/no")
      if confirm == "yes":
            print (f"You have withdrawn {amount}")
            print (End)
      else: print (End)


if correct_pin:
  print ("You have entered the correct pin. Your balance is {} GBP". format(balance))
  cash_withdraw = input ("Would you like to make a withdrawl transaction? Please select Y / N")
  if  cash_withdraw  == "y":
    withdraw()
  else: print(End)











