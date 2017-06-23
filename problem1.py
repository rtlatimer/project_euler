'''for x in range(1000):
	threemath = x / 3
	threes = []
	fives = []
	if (x % 3) == 0:
		threes.append(x)
	if (x % 5) == 0:
		fives.append(x)
print threes, fives'''

#answer = sumthrees + sumfivess
threesfives = []
for x in range(1000):
	if x % 3 == 0 or x % 5 == 0:
		threesfives.append(x)
answer = sum(threesfives)

print threesfives
print answer