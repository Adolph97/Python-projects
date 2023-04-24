# name = input("What is the name of the student? ")
# grade = input("What was the score of the student? ")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
name=open("Names.txt",'r').readlines()
grade=open("Grades.txt",'r').readlines()
names = []
grades = []
for n in name:
	names.append(n.rstrip("\n"))
for g in grade:
	grades.append(g.rstrip("\n"))

# while True:
# 	name=input("Student name: ")
# 	if name == "exit":
# 		break
	# grade=int(input("Score: "))
	# if int(grade) >= 70:
	# 	print(name, "got an A")
	# elif int(grade) >= 60:
	# 	print(name, "got a B")
	# elif int(grade) >= 50:
	# 	print(name, "got a C")
	# elif int(grade) >= 45:
	# 	print(name, "got a D")
	# elif int(grade) < 45:
	# 	print(name, "got an F")

for i in range(len(names)):
	if int(grades[i]) >= 70:
		print(names[i], "got an A with ",grades[i])
	elif int(grades[i]) >= 60:
		print(names[i], "got a B with ",grades[i])
	elif int(grades[i]) >= 50:
		print(names[i], "got a C with ",grades[i])
	elif int(grades[i]) >= 45:
		print(names[i], "got a D with ",grades[i])
	elif int(grades[i]) < 45:
		print(names[i], "got an F with ",grades[i])
