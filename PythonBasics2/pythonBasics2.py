# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
  count = 0
  if (n > 0):
    for num in range(1, n + 1):
      if num % 3 == 0:
        count += 1
  return count


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  rep_char = ""
  rep_count = 0
  curr_char = ""
  curr_count = 0

  for char in s:
    if rep_char == "":
      rep_chat = char
      rep_count += 1
      curr_char = char
      curr_count + 1

    if char == curr_char:
      curr_count += 1
    else:
      if curr_count >= rep_count:
        rep_char = curr_char
        rep_count = curr_count
      curr_char = char
      curr_count = 1

    if curr_count >= rep_count:
      rep_char = curr_char
      rep_count = curr_count
  return rep_char


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  string = s.upper().replace(' ', '')

  for index in range(len(string)):
    if (string[index] != string[len(string) - 1 - index]):
      return False
  return True
