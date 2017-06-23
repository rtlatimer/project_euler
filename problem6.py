'''The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

# Find 1^2 + 2^2 + ... 100^2 = sumofsquares
# Then find (1 + 2 + ... + 100)^2 = squareofsum
# Then squareofsum - sumofsquares

squares = []
for x in range(1,101):
	squared = x * x
	squares.append(squared)
sum_of_squares = sum(squares)
print "Sum of Squares: ", sum_of_squares

sums = []
for x in range(1,101):
	sums.append(x)
summed = sum(sums)
square_of_sum = summed ** 2
print "Square of Sum: ", square_of_sum

difference = square_of_sum - sum_of_squares
print "Difference: ",difference