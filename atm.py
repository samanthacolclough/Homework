Task 1
Question 1 GIT WORKFLOW FUNDAMENTALS
Working Directory:  A working tree or working directory is the area which contains files that are currently being worked on. This is where files are located when you are able to modify and view them.  
Staging Area: This is the area where files are stored before they are committed. The staging area can also be called the index and will compare files found in the working directory in the repository. When changes are made in the working directory/ work tree the index will mark the file a modified before it is committed.
Local Repo (head): A local repository that is stored on your machine/ computer.
Remote repo (master): A repository that is stored on a remote computer 

WORKING DIRECTORY STATES:
 · Staged: This is a file that is being prepared for a commit. Git only allows users to commit certain changes while inbetween 'commits', so while your piece of work is in this stage, it is in the 'staging area' and is being 'staged'. 
 · Modified: A modified working state is when work or changes have been made to a file. Modified work will contain changes that have been made since the last commit, while continuing to 'modify' this work the user will chose what parts to 'stage', and then eventually comit to all of those staged changes.  
 
Committed GIT COMMANDS: 
· Git add: This is a change that is made in the staging area to a file that is yet to be committed. These changes however do not affect the repository until the commit command is ran. 
  
· Git commit: This will save all modified changes/ updates that are in the staging area, these are known as 'staged' changes. When GIT commit is executed it will return a snapshot of committed changes from the staging area into the reposioty.

· Git push: Git push is a command that enables a commit and shares committed work into a repository. When working on code we are using our local machines, git hub enables us to share a ‘committed’ version of this code and ‘pushes’ it to be saved into a remote repository. Git push can be compared to ‘backing up’ our work to a remote area which can later be accessed remotely without our local machines.
  
· Git fetch: The git fetch is the counter part of git push. This command allows us to download commits that have been made and stored into the remote repository into your local repo. Fetching is used when you would like to view work which has been shared into your repository. This could be work that you have completed yourself, or work that has been completed by a peer that can be ‘fetched’ by yourself so you are able to modify it. When you have finished completing/ viewing this work you will then have the option to ‘commit’ and then ‘push’ to share an updated version. 
  
· Git merge: Git merge is a function that will allow a user to combine 2 different branches on git. Merge will take committed changes from on branch and integrates this information and data with another branch that is being worked on. 


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











