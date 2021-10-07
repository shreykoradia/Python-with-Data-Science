numbers = [1, 2, 3, 4, 5]

def square(number):
	return number ** 2

squaring_iterator = map(square, numbers)
squared_numbers = list(squaring_iterator)

print(squared_numbers)