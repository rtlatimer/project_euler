'''Problem 10 
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''

# Create function that checks if a number is prime and under 2 million
# Create variable = 0
# If number is prime & under 2 mil, variable += number

def is_prime(number):
	if number == 5:
		return True
	elif number == 1 or number % 2 == 0 or number % 5 == 0:
		return False
	prime = 3
	while prime<number**.5+1:
		if number % prime == 0:
			return False
		prime += 2
	return True

prime_sum = 2	
for num in xrange(1,2000000,2):
	if is_prime(num):
		prime_sum += num

print prime_sum

		