from symbols import CORNER, LINE, INTERSECTION as INTER, MISC, EYE, MOUTH, NOSE, EAR, HAT, TOY 
def equal(actual, expected):
	return actual.upper() == expected.upper()

def printPet(name, mood):
	print("pet will print here")

def printStats(name, mood, hunger):
	print("stats will go here")

def getSymbols():
	for item in CORNER:
		print(item + " " + CORNER[item])

	for item in LINE:
		print(item + " " + LINE[item])

	for item in INTER:
		print(item + " " + INTER[item])

	for item in MISC:
		print(item + " " + MISC[item])

	for item in EYE:
		print(item + " " + EYE[item])

	for item in MOUTH:
		print(item + " " + MOUTH[item])

	for item in NOSE:
		print(item + " " + NOSE[item])

	for item in EAR:
		print(item + " " + EAR[item])

	for item in HAT:
		print(item + " " + HAT[item])

	for item in TOY:
		print(item + " " + TOY[item])



		




