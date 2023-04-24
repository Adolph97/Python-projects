import random
print("...Rock!...")
print("...Paper!...")
print("...Scissor!...")
player1_wins=0
computer_wins=0
winning_score = 3                       

while player1_wins < 2 and computer_wins < 2:
	print(f"Score is player1: {player1_wins} - computer:{computer_wins}")
	player1=input("please enter player1's move: ").title()
	if player1 == "Exit":
		break
	# try:
		
	# except ValueError:
	# 	print("please type a valid move")
	computer=random.randint(0,2)
	if computer == 0:
		computer = "Rock"
		print("Rock")
	elif computer == 1:
		computer = "Paper"
		print("Paper")
	else:
		computer = "Scissor"
		print("Scissor")
	if player1 == computer:
		print("It's a tie!")
	if player1 == "Rock":
		if computer == "Paper":
			print("computer wins!")
			computer_wins+=1
		elif computer == "Scissor":
			print("player1 wins!")
			player1_wins+=1
	elif player1 == "Paper":
		if computer == "Rock":
			print("player1 wins!")
			player1_wins+=1
		elif computer == "Scissor":
			print("computer wins!")
			computer_wins+=1
	elif player1 == "Scissor":
		if computer == "Rock":
			print("computer wins!")
			computer_wins+=1
		elif computer == "Paper":
			print("player1 wins!")
			player1_wins+=1
	else:
		print("something went wrong!")
if player1_wins > computer_wins:
	print("CONGRATS! player1 wins!")
else:
	print("Darn! computer wins")
print(f"player1: {player1_wins} - computer:{computer_wins}")