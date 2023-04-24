def moreAge():
	currentTime = datetime.now()
	totalDays = currentTime - date_of_birth
	years = (totalDays.total_seconds())/(365.242*24*3600)
	yearsInt = int(years)

	months = (years - yearsInt) * 12
	monthsInt = int(months)

	days = (months - monthsInt)*(365.242/12)
	daysInt=int(days)

	hours = (days - daysInt)*24
	hoursInt = int(hours)

	minutes = (hours - hoursInt)*60
	minutesInt = int(minutes)

	seconds = (minutes - minutesInt)*60
	secondsInt = int(seconds)

	print("You are {} years old, {} months, {} days, {} hours, {} minutes, {} seconds old".format(yearsInt,monthsInt,daysInt,hoursInt,minutesInt,secondsInt))

FName = input("Please type your first name: ")
LName = input("Please type your last name: ")
print("Hello",FName,LName)
# age = input("What's your age in years? ")
from datetime import datetime, date
print("Your date of birth (dd mm yyyy)")
date_of_birth = datetime.strptime(input("--->"), "%d %m %Y")

def calc_age(born):
	today = date.today()
	return today.year - born.year 

age = calc_age(date_of_birth)
print(age)
print("Would you like to know in detail how old you are to the exact seconds?")
print("Press 'y' to continue or 'n' to exit this program")
nextInput = input()
if nextInput == 'Y' or nextInput =='y':
	moreAge()
else:
	print("Thanksfor using this program", FName+LName, " Goodbye!")
