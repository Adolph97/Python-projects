def tempF(degC):
	degF = (degC*9/5)+32
	print(degF) 
	pass

def tempC(degF):
	degC = (degF-32)*5/9
	print(degC) 

def temp():
	print("please insert the type of conversion you would like to make")
	print("Press 1 in order to convert from degree Celsius to degree Fahrenheit, and 2 for vice versa")
	print("1. DegreeC to DegreeF.\n2. DegreeF to DegreeC.\n3. To exit")
	number=int(input("please type a number for the selection of an option: "))
	while number != 3:
		if number == 1:
			print("please insert the temperature in DegreeC or type exit to go back to the main menu")
			degC=input("degC: ")
			if degC == str("exit"):
				temp()
			else:
				tempF(int(degC))

		elif number == 2:
			print("please insert the temperature in DegreeF or type exit to go back to the main menu")
			degF=input("degF: ")
			if degF == str("exit"):
				temp()
			else:
				tempC(int(degF))

	exit()
temp()