from random import randint
from gamefunctions import gameVars

def winorlose(status):

	print("You", status,"! " "play again?")
	choice = input("Y / N?")

	if choice == "Y" or choice == "y":
			
			gameVars.player_lives = 1
			gameVars.computer_lives = 1
			player = False
			gameVars.computer = gameVars.choices [randint(0, 2)]

	elif choice == "N" or  choice == "n":
			print("You chose to quit. Better luck next time.")
			exit()
	else:
			print("Make a valid choice. Yes or No.")
			# recursion = claiing a function from inside itself
			winorlose(startus)
