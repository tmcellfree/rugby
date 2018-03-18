###################################################################
# Script to calculate trys/conversions/penalties from a rugby match
###################################################################

###################################################################
# In rugby, joining a game late makes it tough to tell wha the 'type' of scores happened
# There is a rugby equation to solve this problem!
# 5x + 7y + 3z = score
# where x = unconverted tries, y = converted tries, z = penalties (or drop goals), score = user input
# x, y, z, score are positive integers
###################################################################
score = input('Enter the score: ')
# constrain the range of possibilities for iteration
max_tries = int(score)//5
max_converted = int(score)//7
max_penalty = int(score)//3

print 'The score is:', score

possibilities = 0
#assume zero unconverted tries
print 'Trying...', len(range(max_penalty+1))*len(range(max_tries+1))*len(range(max_converted+1)), 'permutations'
for i in range(max_penalty+1):
	# print 'Penalties', i     # Only needed for spotting errors
	if i == 0:
		t = 0
		s = 0 
		if 3*int(i) + 5*int(t) + 7*int(s) == int(score) and score > 0:    # AKA the rugby equation! 
			print'Converted Tries:', s, 'Tries:', t, 'Penalties: (or Drop Goals):', i 
			possibilities = possibilities+1                 # Keeping track of the different valid solutions to the rugby equation	
	for t in range(max_tries+1):
		# print 'unconverted tries', t     # Only needed for spotting errors
		if i == 0 and t == 0:
			s = 0
			if 3*int(i) + 5*int(t) + 7*int(s) == int(score) and score > 0:    # AKA the rugby equation! 
				print'Converted Tries:', s, 'Tries:', t, 'Penalties: (or Drop Goals):', i 
				possibilities = possibilities+1                 # Keeping track of the different valid solutions to the rugby equation
		for s in range (max_converted+1):
			# print 'converted tries', s      # Only needed for spotting errors
			if 3*int(i) + 5*int(t) + 7*int(s) == int(score) and score > 0:    # AKA the rugby equation! 
				print'Converted Tries:', s, 'Tries:', t, 'Penalties: (or Drop Goals):', i 
				possibilities = possibilities+1                 # Keeping track of the different valid solutions to the rugby equation
if possibilities == 0:
	print score, 'is not a valid score'
print 'Total of', possibilities, 'possible combinations!'
print 'Enjoy the game!'