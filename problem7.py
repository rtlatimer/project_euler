'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?'''

# Create list of all prime numbers.
# Print out prime_number(10001)

'''def is_prime(num):
    """Returns True if the number is prime
    else False."""
    if num == 0 or num == 1 or num % 2 == 0:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True'''

'''primey1 = filter(is_prime, xrange(1, 10000, 2))
print len(primey1)

primey2 = filter(is_prime, range(10000, 20000))
print len(primey2)

primey3 = filter(is_prime, range(20000, 30000))
print len(primey3)

primey4 = filter(is_prime, range(30000, 40000))
print len(primey4)

primey5 = filter(is_prime, range(40000, 50000))
print len(primey5)

primey6 = filter(is_prime, range(50000, 60000))
print len(primey6)

primey7 = filter(is_prime, range(60000, 70000))
print len(primey7)'''

'''primey8 = filter(is_prime, range(70000, 80000))
print len(primey8)'''

'''primey9 = filter(is_prime, xrange(80001, 90000, 2))
print len(primey9)'''

'''primey10 = filter(is_prime, xrange(90001, 100000, 2))
print len(primey10)'''

'''primey11 = filter(is_prime, xrange(100001, 107000, 2))
print len(primey11)
print primey11[408]'''

import time
 
def fast_nth_prime(n, limit=125000):
    if limit % 2 != 0: limit += 1
    primes = [True] * limit
    primes[0],primes[1] = [None] * 2
    count = 0 # how many primes have we found?
    for ind,val in enumerate(primes):
        if val is True:
            # sieve out non-primes by multiples of known primes
            primes[ind*2::ind] = [False] * (((limit - 1)//ind) - 1)
            count += 1
        if count == n: return ind
    return False
 
start = time.time()
prime = fast_nth_prime(10001)
elapsed = (time.time() - start)
 
print "found %s in %s seconds." % (prime,elapsed)

import time
 
# function to factor a given positive integer n
def is_prime(n):
    # look for factors of 2 first
    if n % 2 == 0: return False
    # now look for odd factors
    p = 3
    while p < n**0.5+1:
        if n % p == 0: return False
        p += 2
    return True
 
def nth_prime(n):
    prime = 2
    count = 1
    iter = 3
    while count < n:
        if is_prime(iter):
            prime = iter
            count += 1
        iter += 2
    return prime
 
start = time.time()
prime = nth_prime(10001)
elapsed = (time.time() - start)
 
print "found %s in %s seconds" % (prime,elapsed)