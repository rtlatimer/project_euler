'''Problem 17 
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.'''



# Number of letters in each number from 0 to 19
single = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
# 0,10,20,30,40,50,60,70,80,90
tens = [0,3,6,6,5,5,5,7,6,6]

hundred = 7
thousand = 8

total = 0
for x in range(1,1000):
	c = x % 10 # singles digit
	b = ((x % 100) - c) / 10 # tens digit
	a = ((x % 1000) - (b * 10) - c) / 100 # hundreds digit

	if a != 0:
		total += single[a] + hundred
		if b != 0 or c != 0:
			total += 3
	if b == 0 or b == 1:
		total += single[b * 10 + c]
	else:
		total += tens[b] + single[c]
total += single[1] + thousand

print total



