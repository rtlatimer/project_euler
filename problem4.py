# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2 digit numbers is 9009 = 91 x 99
# Find the largest palindrome made from the product of two 3-digit numbers.

# Intuition says multiply every combination of 3-digit numbers,
# Check if a solution is a palindrome & store it to a list if yes
# Return max number from list

palindromes = []
for x in range(1000,99,-1):
	for y in range(1000,99,-1):
		product = x * y
		if str(product) == str(product)[::-1]:
			palindromes.append(product)

#print palindromes
palindrome_ints = [int(i) for i in palindromes]
print max(palindrome_ints)

'''def is_palindrome(num):
	if str(num) == str(num)[::-1]:
		return True
	else:
		return False


print is_palindrome(100)'''
