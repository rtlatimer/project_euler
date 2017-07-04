'''Problem 26 
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.'''

'''fractions = []
for x in range(1,200):
	quotient = 1./x
	fractions.append(quotient)

print fractions

patterns = {}
for length in range(1, len(fractions)):
	found_patterns = {}
	for start in range(0, len(fractions) - length + 1):
		found_patterns[start] = tuple(patterns[start:start+length])
	candidates = set(found_patterns.values())
	if len(candidates) != len(found_patterns.values()):
		patterns = found_patterns[10]
	max_len = len(patterns) / 2+1
	for x in range(2,max_len):
		if patterns[0:x] == patterns[x:2*x]:
			jimmy = x
print jimmy'''

def repeating(num, den):
    for length in range(1, den):
        if 1 == 10**length % den:
            return length
    return 0

longest_pattern = max(repeating(1, x) for x in range(2,1001))
print([x for x in range(2,1001) if repeating(1, x) == longest_pattern][0])





