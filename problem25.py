'''Problem 25 
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?'''

fibs = [1,1]
for x in range(2,5000):
	fibs.append(fibs[x-1] + fibs[x-2])

#for fib in fibs:
	#print len(str(fib))

print fibs[4781]

thousand = [i for i,x in enumerate(fibs) if len(str(x)) == 1000]
print thousand

