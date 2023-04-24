import os
def prompt():
	print(f"you got only {right} options correctly and {wrong} options incorrectly!")
	print("Thanks for using this program.")

def leave():
	print("please type 'exit' to leave the program")

mem = []
no = 1
trial = 1
right = 0
wrong = 0
userno = 1
print("When you are done with entering the words or numbers you want to memorize, please type done to exit the listing mode")

leave()
while True:
	user = str(input(f"What are the things you'd like to memorize? ({userno})")).lower()
	if user == str("done"):
		break
	if user == str("exit"):
		exit()
	mem.append(user)
	userno += 1

os.system('cls')

print("When you can't remember the word memorized for the number, type done to exit the memorization")
leave()

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
			if trial == 3:
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