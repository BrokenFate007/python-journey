right_count = 0
n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
while n == "right" or n == "Right":
   right_count += 1
   if right_count ==1:
      n = input("You are in the Lost Forest\n****************\n****************\n :(\n****************\n****************\nGo left or right? ")
   if right_count >= 2:
      n = input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┻━┻\n****************\n****************\nGo left or right? ")
print("\nYou got out of the Lost Forest!\n\o/")
