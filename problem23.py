'''Problem 23 
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.'''

def proper_divisors(num):
	num_list = []
	for x in range(1,num/2 + 1):
		if num % x == 0:
			num_list.append(x)
	return sum(num_list)

abundants = []
for x in range(12,28123):
	if proper_divisors(x) > x:
		abundants.append(x)

abundant_dict = {x:x for x in abundants}

sum_list = [1]
for x in range(2, 28123):
    booly = True
    for y in abundants:
        if y < x:
            if (x-y) in abundant_dict:
                booly = False
                break
        else:
        	break
    if booly == True:
    	sum_list.append(x)

print sum_list
print sum(sum_list)




