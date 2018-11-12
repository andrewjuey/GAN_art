import rhinoscriptsyntax as rs
"""
Script written by Ezio Blasetti
Script copyrighted by ahylo studio
Script version Thursday, January 20, 2011 12:59:05 PM
From Wolfram MathWorld: A cellular automaton is a collection of "colored" cells on a grid of specified shape that evolves through a number of discrete time steps according to a set of rules based on the states of neighboring cells. The rules are then applied iteratively for as many time steps as desired. Von Neumann was one of the first people to consider such a model, and incorporated a cellular model into his "universal constructor." Cellular automata were studied in the early 1950s as a possible model for biological systems. Comprehensive studies of cellular automata have been performed by S. Wolfram starting in the 1980s, and Wolfram#s fundamental research in the field culminated in the publication of his book A New Kind of Science (Wolfram 2002) in which Wolfram presents a gigantic collection of results concerning automata, among which are a number of groundbreaking new discoveries.
This code will produce a height-field surface with the texture of 1 out of the 256 elementary cellular automaton rules.
The code will ask which rule (0-255) to use, and for the desired length and width of the surface.
"""

# This function takes the 1 dimensional cellular automaton ruleset and a collection of 0s and 1s and returns a new collection by applying the ruleset
# Define Custom Function ApplyRules (2 inputs: the Ruleset as binary, an array of 0s and 1s of the Previous Generation)
def ApplyRules(arrBinary,arrStates):
	# Setup:
	# Define a new list to contain the States of the New Generation
	arrNewStates = []
	# Loop for i = 0 to the Number of Elements in the array of the Previous Generation
	for i in range(len(arrStates)):
		# The State of the Current Cell will be the (i) element in the array of the Previous Generation
		intCurrentCell = arrStates[i]
		# Cylidrical Space:
		# If i is 0 Then
		if i==0 :
			# The State of the Left Cell will be the last element in the array of the Previous Generation 
			intLeftCell = arrStates[-1]
			# Else
		else :
			# The State of the Left Cell will be the (i-1) element in the array of the Previous Generation 
			intLeftCell = arrStates[i-1]
			# End If
		# If i is the last index in the array of the Previous Generation Then
		if i==len(arrStates)-1 :
			# The State of the Right Cell will be the first element in the array of the Previous Generation 
			intRightCell = arrStates[0]
			# Else
		else :
			# The State of the Right Cell will be the (i+1) element in the array of the Previous Generation 
			intRightCell = arrStates[i+1]
			# End If
		# The Rules:
		# If the State of the Left Cell is "1" and of the Current Cell is "1" and of the Right Cell is "1" Then
		if intLeftCell == 1 and intCurrentCell == 1 and intRightCell == 1 :
			# The Next Element in the New Generation will be the (0) element in the binary Ruleset
			arrNewStates.append(arrBinary[0])
			# End If
		# If the State of the Left Cell is "1" and of the Current Cell is "1" and of the Right Cell is "0" Then
		if intLeftCell == 1 and intCurrentCell == 1 and intRightCell == 0 :
			# The Next Element in the New Generation will be the (1) element in the binary Ruleset
			arrNewStates.append(arrBinary[1])
			# End If
		# If the State of the Left Cell is "1" and of the Current Cell is "0" and of the Right Cell is "1" Then
		if intLeftCell == 1 and intCurrentCell == 0 and intRightCell == 1 :
			# The Next Element in the New Generation will be the (2) element in the binary Ruleset
			arrNewStates.append(arrBinary[2])
			# End If
		# If the State of the Left Cell is "1" and of the Current Cell is "0" and of the Right Cell is "0" Then
		if intLeftCell == 1 and intCurrentCell == 0 and intRightCell == 0 :
			# The Next Element in the New Generation will be the (3) element in the binary Ruleset
			arrNewStates.append(arrBinary[3])
			# End If
		# If the State of the Left Cell is "0" and of the Current Cell is "1" and of the Right Cell is "1" Then
		if intLeftCell == 0 and intCurrentCell == 1 and intRightCell == 1 :
			# The Next Element in the New Generation will be the (4) element in the binary Ruleset
			arrNewStates.append(arrBinary[4])
			# End If
		# If the State of the Left Cell is "0" and of the Current Cell is "1" and of the Right Cell is "0" Then
		if intLeftCell == 0 and intCurrentCell == 1 and intRightCell == 0 :
			# The Next Element in the New Generation will be the (5) element in the binary Ruleset
			arrNewStates.append(arrBinary[5])
			# End If
		# If the State of the Left Cell is "0" and of the Current Cell is "0" and of the Right Cell is "1" Then
		if intLeftCell == 0 and intCurrentCell == 0 and intRightCell == 1 :
			# The Next Element in the New Generation will be the (6) element in the binary Ruleset
			arrNewStates.append(arrBinary[6])
			# End If
		# If the State of the Left Cell is "0" and of the Current Cell is "0" and of the Right Cell is "0" Then
		if intLeftCell == 0 and intCurrentCell == 0 and intRightCell == 0 :
			# The Next Element in the New Generation will be the (7) element in the binary Ruleset
			arrNewStates.append(arrBinary[7])
			# End If
		# End Loop
	# Return the New Generation array
	return arrNewStates
	# End ApplyRules Function
# This function translates an integer from 0 to 255 to a binary string. Example: 30 -> 0,0,0,1,1,1,1,0
# Define Custom Function DecimalToBinary (1 input: integer, the Number of the Ruleset from 0 to 255)
def DecimalToBinary(intRuleset):
	# Setup:
	# Define a new empty list variable (arrResult) which will contain the Result
	arrResult = []
	# Define a new integer variable (intVal) to Temporary store the Number of the Ruleset and to do calculations with
	intVal    = intRuleset
	# Define a new integer variable (intExp) to store the various Powers of 2, and make it equal to 256
	intExp    = 256
	# Calculate the binary String:
	# While intExp is greater of equal to 1
	while intExp >= 1 :
		# If intVal is greater of equal to intExp Then
		if intVal >= intExp :
			# The intVal will be equal what it was minus the intExp 
			intVal = intVal - intExp
			# The strResult will be added a "1" on the right side of the string
			arrResult.append(1)
		# Else
		else :
			# the strResult will be added a "0" on the right side of the string
			arrResult.append(0)
		# End If
		# The intExp will be half of what it was
		intExp = intExp / 2
		# End the While loop
	# The arrResult will be the last 8 digits of what it was - 16 including the commas
	# Return the arrResult
	return arrResult[-8:]
	# End Custom Function DecimalToBinary
# Define Main Subroutine
def Main():
	# Get User Input:
	# Get the Ruleset (integer, from 0 to 255, the identifier of the elementary cellular automaton ruleset)
	intRuleset     = rs.GetInteger("Please type the ruleset number for the cellular automata - Wolfram",30,0,255)
	# Get the Number of Generations (integer, the amount of times the ruleset should be applied)
	# (and consequently the total length of the resulting surface - default value 50, minimum value 1)
	intGenerations = rs.GetInteger("Please type the ammount of generations to compute",51, 1)
	# Get the Number of Elements in each Generation (integer, odd, how many cells should each generation have)
	# (and consequently the total width of the resulting surface - default value 50, minimum value 5)
	intElements    = rs.GetInteger("Please type the ammount of cells - elements in each generation",51, 5)
	# Setup:
	# Call the DecimalToBinary Function (input: the Ruleset as an integer from 0 to 255)
	arrBinary      = DecimalToBinary(intRuleset)
	# Define a dynamic array to contain the coordinates of all the points of the surface (array, one dimensional, size: currently null)
	arrPoints      = []
	# Setup the Initial Generation with all 0s and a 1 in the middle:
	# Make sure the Number of Elements in each Generation is an odd Number - so that there is a "middle"
	if (intElements % 2 == 0):
		intElements = intElements + 1
		rs.Print("I have increased the Number Of Elements in each Generation by 1")
	# Define a new array to contain the State of each cell (array, one dimensional, size: Number of Elements minus one)
	arrStates      = []
	# Loop for i = 0 to the Number of Elements minus one
	for i in range(intElements):
		# if currently i is half of the Number of Elements minus one Then
		if (i==(intElements-1)/2):
			# The array of the States at the position i will be 1
			arrStates.append(1)
			# Else
		else :
			# The array of the States at the position i will be 0
			arrStates.append(0)
			# End If
		# End Loop (i)
	# Apply the Rules:
	# Loop for i = 0 to the Number of Generations
	for i in range(intGenerations):
		# Loop for j = 0 to the Number of Elements in each Generation
		for j in range(intElements):
			# If the current [j] State in the array of states is 0 Then
			if arrStates[j]==0 :
				# The last element in the array of points will be an array of 3 integers [x = j, y = -i, z = 0]
				arrPoints.append([j,-i,0])
				# else :
			else :
				# The last element in the array of points will be an array of 3 integers [x = j, y = -i, z = 1]
				arrPoints.append([j,-i,2])
				# End If
			# End Loop (j)
		# Call the ApplyRules Function (custom function, input: the Ruleset as binary, the array of States as an array of 0s and 1s)
		arrNewStates = ApplyRules(arrBinary, arrStates)
		# Replace the content in the array of States with the array from the ApplyRules Function
		for j in range(len(arrStates)):
			arrStates[j] = arrNewStates[j]
		# End Loop (i)
	# Draw the Surface From a Point Grid (input: the length and width of the surface in an array, the array of coordinates of the points)
	# rs.AddSrfPtGrid([intGenerations,intElements],arrPoints)
	rs.AddSrfControlPtGrid([intGenerations,intElements],arrPoints)
	# End Main Subroutine
Main()
