'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

# Computationally heavy, but start at 20 and divide each number by nums 1-20
# Check if number % 1-20 == 0
# Return smallest number

test = range(2,21)

def divide(num):
    for num in xrange(2520, 999999999, 2520):
        if all(num % i == 0 for i in test):
            return num
answer = divide(20)
print answer


