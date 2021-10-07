# A school method based Python3 program
# to check if a number is prime

# function check whether a number
# is prime or not

n = int(input("Enter a valid Number"))
def isPrime(n):

	# Corner case
	if (n <= 1):
		return False

	# Check from 2 to n-1
	for i in range(2, n):
		if (n % i == 0):
			return False

	return True


# Driver Code
if isPrime(n):
	print("true")
else:
	print("false")
