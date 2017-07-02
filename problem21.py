'''Problem 21 
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.'''

def proper_divisors(num):
	num_list = []
	for x in range(1,num/2 + 1):
		if num % x == 0:
			num_list.append(x)
	return num_list

amicable_numbers = []
for x in range(10000):
	sum_x = sum(proper_divisors(x))
	y_list = sum(proper_divisors(sum_x))
	if x == y_list and x != sum_x:
		if x not in amicable_numbers:
			amicable_numbers.append(x)
		if sum_x not in amicable_numbers:
			amicable_numbers.append(sum_x)

print "List of Amicable Numbers: ",amicable_numbers
print "Sum of Amicable Numbers: ", sum(amicable_numbers)


