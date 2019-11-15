from random import randint
from gamefunctions import winlose, gameVars, rpsfunctions


while gameVars.player is False:
	print("===========================================")
	print("Computer lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("===========================================")
	print("Chose your weapon!\n")
	player = input("choose rock, paper, or scissors: \n")

	print("computer: ", gameVars.computer, "player: ", player)
	
	print("------------------------------------------------------")
	rpsfunctions.compare(player, gameVars.computer)
	print("------------------------------------------------------")
#=========================================================================================================
	if gameVars.player_lives is 0:
		winlose.winorlose("lost")
		
	elif gameVars.computer_lives is 0:
		winlose.winorlose("won")
		
	else:
		player = False
		gameVars.computer = gameVars.choices[randint(0,2)]