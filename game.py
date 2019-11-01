from random import randint

choices=["rock","scissors","paper"]
#let ai make a choice
computer=choices[randint(0,2)]

#set up a gae loop to so we don't have to reset
player = False

while player is False:
	player = input("choose rock, paper, or scissors: \n")

	# start doing some logic and condition checking
	print("computer: ", computer, "player: ", player)
	# always check a breaking condition first
	if player == computer:
		#we have a tie, no point in goin gany further
		print("tie, no one wins! try again")
	elif player== "quit":
		print("you chose to quit, quitter.")
		exit()

	elif player == "rock": 
		if computer == "paper":
			print("you lose!", computer, "covers", player, "\n")
		else:
			print("you won!", player, "smashes", computer, "\n")

	elif player == "paper": 
		if computer == "scissors":
			print("you lose!", computer, "cuts", player, "\n")
		else:
			print("you won!", player, "covers", computer, "\n")
	elif player == "scissors": 
		if computer == "rock":
			print("you lose!", computer, "smashes", player, "\n")
		else:
			print("you won!", player, "cuts", computer, "\n")
	player = False
	computer=choices[randint(0,2)]