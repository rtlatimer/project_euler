'''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''

# Create function that checks whether combination is Pythagorean
# Create a tuple from 0-1000 where a<b<c and a+b+c = 1000
# If one of the combinations satisfies first function, return a,b,c

def pythag(aval,bval,cval):
	if aval**2 + bval**2 == cval**2:
		return True

for a in range(1,1000):
	for b in range(a,1000-a):
		for c in range(b,1000-b):
			if a + b + c == 1000:
				if pythag(a,b,c):
					print (a,b,c)
					print a*b*c

		

