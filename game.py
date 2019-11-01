from random import randint

choices=["rock","scissors","paper"]

#adding lives -> when someone gets to 0 you win or lose
player_lives = 1
computer_lives = 1

#let ai make a choice
computer=choices[randint(0,2)]

#set up a game loop to so we don't have to reset
player = False

def winorlose(status):
	# print("called win or lose", status)
	print("You", status)
	choice = input("Y / N?")

	if choice == "Y" or choice == "y":
			global player_lives 
			global computer_lives
			global player 
			global computer 
			# reset the game and start all over again
			player_lives = 1
			computer_lives = 1
			player = False
			computer = choices [randint(0, 2)]

	elif choice == "N" or  choice == "n":
			print("You chose to quit. Better luck next time.")
			exit()
	else:
			print("Make a valid choice. Yes or No.")




while player is False:
	print("===========================================")
	print("Computer lives:", computer_lives, "/1")
	print("Player lives:", player_lives, "/1")
	print("===========================================")
	print("Chose your weapon!\n")
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
			player_lives = player_lives -1
		else:
			print("you won!", player, "smashes", computer, "\n")
			computer_lives = computer_lives -1

	elif player == "paper": 
		if computer == "scissors":
			print("you lose!", computer, "cuts", player, "\n")
			player_lives = player_lives -1
		else:
			print("you won!", player, "covers", computer, "\n")
			computer_lives = computer_lives -1

	elif player == "scissors": 
		if computer == "rock":
			print("you lose!", computer, "smashes", player, "\n")
			player_lives = player_lives -1
		else:
			print("you won!", player, "cuts", computer, "\n")
			computer_lives = computer_lives -1
#=========================================================================================================
	if player_lives is 0:
		winorlose("lost")
		# print("You lost! LOSER. Would you like to play again?")
		# choice = input("Y / N?")

		# if choice == "Y" or choice == "y":
		# 	player_lives = 1
		# 	computer_lives = 1
		# 	player = False
		# 	computer = choices[randint(0, 2)]

		# elif choice == "N" or  choice == "n":
		# 	print("You chose to quit. Better luck next time.")
		# 	exit()
		# else:
		# 	print("Make a valid choice. Yes or No.")

	elif computer_lives is 0:
		winorlose("won")
		# print("You won! Would you like to play again?")
		# choice = input("Y / N?")
			
		# if choice == "Y" or choice == "y":
		# 	player_lives = 1
		# 	computer_lives = 1
		# 	player = False
		# 	computer = choices[randint(0, 2)]

		# elif choice == "N" or  choice == "n":
		# 	print("You chose to quit. goodbye.")
		# 	exit()
		# else:
		# 	print("Make a valid choice. Yes or No.")
	else:
		player = False
		computer=choices[randint(0,2)]