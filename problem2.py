fibs = [0,1]
for x in range(2,40):
	fibs.append(fibs[x-1] + fibs[x-2])
#print fibs

evenfibs = []
for i in fibs:
	if i%2 == 0 and i < 4000000:
		evenfibs.append(i)
		#[i for i in fibs if i%2 == 0 and i<4000000000]
#print evenfibs
print fibs
print evenfibs
print sum(evenfibs)
'''def fib(x):
	if x == 0:
		return 0
	elif x == 1:
		return 1
	else:
		return fib(x-1) + fib(x-2)

print fib(11)'''

#answer = sum of fibonaccis less than 4mil where % 2 == 0
