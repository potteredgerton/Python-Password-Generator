import random

lower = ("abcdefghijklmnopqrstuvwxyz")
upper = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = ("1234567890")
symbols = ("!@#$%^&*")

length = int(input("How long should the password be? "))
print()
string = lower + upper

varsym = input("Would you like to include symbols? Y/N ")
if varsym == "Y" or varsym == "y":
  string = string + symbols
  print()
elif varsym == "N" or varsym == "n":
  print()
else:
  print("Please enter either Y or N, do not enter anything else")

varnum = input("Would you like to include numbers? Y/N ")
if varnum == "Y" or varnum == "y":
  string = string + numbers
  print()
elif varnum == "N" or varnum == "n":
  print()
else:
  print("Please enter either Y or N, do not enter anything else")

password = "".join(random.sample(string, length))

print("Your Password is", password)
