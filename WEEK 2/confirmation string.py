# program to check if a string is a palindrome
my_str = 'albohPHOBIA'
# make it suitable for caseless comparisson
my_str = my_str . casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
 print("the string is a palindrome.")
else:
 print("the string is not a palindrome.")