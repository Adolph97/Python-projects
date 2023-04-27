import os	# the operating system module
# function to output the number of right and wrong answers provided
def prompt():
	print(f"you got only {right} options correctly and {wrong} options incorrectly!")
	print("Thanks for using this program.")

# function to output an instruction on how to exit the program
def leave():
	print("please type 'exit' to leave the program")

mem = [] # list to hold the range of words that would be memorized by the user
no = 1 # variable to keep track of the number for each answers requested by the program
trial = 1 # variable to keep track of each tries by the user
right = 0 # variable to keep track of the right answers by the user
wrong = 0 # variable to keep track of wrong answers by the user
userno = 1 # variable to keep track of the number for each of the items to be memorized
print("When you are done with entering the words or numbers you want to memorize, please type 'done' to exit the listing mode")

leave()
while True:
	# The user variable is used to keep track of user's input
	user = str(input(f"What are the things you'd like to memorize? ({userno})")).lower()
	if user == str("done"): # exit command to proceed to the trial phase
		break
	if user == str("exit"): # command to close the program
		exit()
	mem.append(user) # updates the memorization list everytime an input is completed
	userno += 1 # updates the count of the items being memorized

# clears terminal when the loop is broken out of
os.system('cls')

print("When you can't remember the word memorized for the number, type done to exit the memorization")
leave()

# Loop to cross-check the items contained in the list designated for memorization
for i in mem:
	answer = input(f"What was the number {no} item on the list? ").lower()
	if answer == str("done"):
		break
	if answer == str("exit"):
		exit()
	if answer == i:
		print("Yay! you got it!.. On to the next!")
		right += 1
	else:
		trial = 1
		# Condition for 3 tries on each chance given to the user
		while trial < 3:
			print("That's wrong!")
			answer = input(f"what is the number {no} item on the list? ")
			if answer == str("exit"):
				prompt()
				exit()
			if answer == str("back"):
				break
			if answer == i:
				print("That's correct! You got it.....Next.")
				right += 1
				break
			trial += 1
			if trial == 3:	# on 3 tries, the number of wrong answers is updated
				wrong += 1
				if answer == i:
					print("That's correct! You got it.....Next.")
					right += 1
					break
				else:
					print(f"you got the number {no} item on your list wrong")
				
	no += 1
if right == userno:
	print(f"Hurray! You got everything! (all {userno} items correctly\n That's really awesome")
else:
	prompt()