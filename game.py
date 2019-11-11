from functions import equal, printPet, printStats, getSymbols

response = input("Enter pet name: ")

petName = response

while not equal(response, "bye"):
	#printPet(response, 100)

	#print("You said: " + response)
	response = input("Enter text: ")

	getSymbols()