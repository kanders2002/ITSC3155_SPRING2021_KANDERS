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
  mult_of_three = "0"
  high_app = 0

  count_dict = {
    "0":0,
    "3":0,
    "6":0,
    "9":0
  }
  
  for num in range(0, len(n)):
    count_dict[n[num]] = count_dict[n[num]] + 1

  for key in count_dict:
    if count_dict[key] > high_app:
      high_app = count_dict[key]
      mult_of_three = key
  return int(mult_of_three)

# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  
  return_val = 0
  list = []

  longest_dict = {}
  
  for char in s:
    longest_dict[char] = 0
    
  for num in range(0, len(s) - 1):
    if s[num] == s[num + 1]:
      longest_dict[s[num]] = longest_dict[s[num]] + 1
      
  for value in longest_dict.values():
    if value > return_val:
      return_val = value

  for key in longest_dict:
    if longest_dict[key] == return_val:
      list.append(key)
          
  return list


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
