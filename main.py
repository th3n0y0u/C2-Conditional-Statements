# Prompt the user for the amount of cents and store it in a variable 
cents = int(input("Please insert a number of cents: "))
quarters = 0
dimes = 0
nickels = 0
pennies = 0
# Conditional Statements to calculate the number of each type of coin
if(cents > 0):
 if(cents >= 25):
   quarters += cents // 25
   cents %= 25
 if(cents >= 10):
   dimes += cents // 10
   cents %= 10
 if(cents >= 5):
   nickels += cents // 5
   cents %= 5
 if(cents >= 1):
    pennies += cents // 1
    cents //= 1
  
 print("Quarters: " + str(quarters))
 print("Dimes: " + str(dimes))
 print("Nickels: " + str(nickels))
 print("Pennies: " + str(pennies)) 
else:
 print("Please pick a number that's greater then zero or you could just have a negative balance")