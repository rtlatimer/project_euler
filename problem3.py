# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# create list of prime numbers
# divide 600851475143 by those numbers and if % num = 0, then store to a new list
# pull the max num from new list

def is_prime(num):
    """Returns True if the number is prime
    else False."""
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True

primeys = filter(is_prime, range(1, 10000))
#print primeys

goodprimeys = []
for i in primeys:
	if 600851475143 % i == 0:
		goodprimeys.append(i)
print goodprimeys

answer = max(goodprimeys)
print answer