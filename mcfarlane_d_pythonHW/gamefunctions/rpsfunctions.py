
from gamefunctions import gameVars

def compare(player, computer):

	if gameVars.player == gameVars.computer:
			#we have a tie, no point in goin gany further
			print("tie, no one wins! try again")
	elif player == "quit":
		print("you chose to quit, quitter.")
		exit()

	elif player == "rock": 
		if gameVars.computer == "paper":
			print("you lose!", gameVars.computer, "covers", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("you won!", player, "smashes", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "paper": 
		if gameVars.computer == "scissors":
			print("you lose!", gameVars.computer, "cuts", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("you won!", player, "covers", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "scissors": 
		if gameVars.computer == "rock":
			print("you lose!", gameVars.computer, "smashes", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("you won!", player, "cuts", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1