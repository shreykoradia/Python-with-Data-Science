def firstLetterWord(str):

	result = ""

	# Traverse the string.
	v = True
	for i in range(len(str)):
		
		# If it is space, set v as true.
		if (str[i] == ' '):
			v = True

		# Else check if v is true or not.
		# If true, copy character in output
		# string and set v as false.
		elif (str[i] != ' ' and v == True):
			result += (str[i])
			v = False

	return result
	
str = input("Enter the string")
print(firstLetterWord(str))

