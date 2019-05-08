'''A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.'''

list = [ i*j for i in range(99,999) for j in range(99,999) if str(i*j) == str(i*j)[::-1]]

largestPalindrome = max(list)

print(largestPalindrome) #906609

input()