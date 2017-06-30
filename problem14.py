'''Problem 14 
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.'''

longest_chain = []

'''def make_chain(number):
	chain = [number]
	while number > 1:
		if number % 2 == 0:
			number = number/2
			chain.append(number)
		elif number % 2 != 0:
			number = 3*number + 1
			chain.append(number)
	return chain'''

for x in range(1000000):
	chain = [x]
	while x > 1:
		if x % 2 == 0:
			x = x/2
			chain.append(x)
		elif x % 2 != 0:
			x = 3*x + 1
			chain.append(x)	
		if len(chain) > len(longest_chain):
			longest_chain = chain

print longest_chain[0], len(longest_chain)

'''longest_chain = []
if len(chain) > len(longest_chain):
	longest_chain = chain
print longest_chain
print make_chain(x)'''

