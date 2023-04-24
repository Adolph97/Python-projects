interest = float(input("interest"))
principal = int(input("principal"))
time = int(input("months"))
compound = 0

for i in range(time):
	compound = principal+(principal * interest)
	principal = compound
	print("%.2f"%(compound))

#++++++++++++++++++++++++++++++++usinf formular
# compound=principal*pow(1+(interest/12),12*time)
# print(compound)
# n