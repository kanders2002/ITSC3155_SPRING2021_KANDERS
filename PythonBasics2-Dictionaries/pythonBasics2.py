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
  large_app = 0
  """ 
  Above I have created mult_of_three and high_app. In the steps provided, I am requested to return the 
  multiple of three and appearances. mult_of_three represents the multiple of three, while high_app
  represents the largest appearances. 
  """

  count_dict = {
    "0":0,
    "3":0,
    "6":0,
    "9":0
  }
  """ 
  Here I have initialized count_dict which represents the count_threes dictionary. As you can see, I only
  included the multiples of three.
  """
  
  for num in range(0, len(n)):
    count_dict[n[num]] = count_dict[n[num]] + 1
  """ 
  Above is a for loop, which views number of appearances for every multiple of three, as well as values.
  """

  for key in count_dict:
    if count_dict[key] > large_app:
      large_app = count_dict[key]
      mult_of_three = key
  return int(mult_of_three)
  """ 
  Above is a for loop, which actually views the keys. Not only that, but it also finds the most occurring
  appearance.
  """

# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  
  return_val = 0
  list = []
  """ 
  Above is the return_val and list. The assignments states "The return value should now be a list," which
  led to return_val associating with returning value. The returning value is the most frequently appearing
  character. The list is simply referring to the list, which will be updated later.
  """

  longest_dict = {}

  """ 
  Here I have initialized longest_dict which represents the count_threes dictionary. The characters
  will be added later.
  """

  for char in s:
    longest_dict[char] = 0
  """
  Above I created a for loop. The purpose of the loop is to add to the dictionary. Specifically, add
  the characters to the longest_dict.
  """
    
  for num in range(0, len(s) - 1):
    if s[num] == s[num + 1]:
      longest_dict[s[num]] = longest_dict[s[num]] + 1

  """
  Above I created a for loop. The purpose of the loop is to count the consecutive repeats, as well as 
  modify longest_dict.
  """
      
  for value in longest_dict.values():
    if value > return_val:
      return_val = value
  """
  Above I created a for loop. The purpose of the loop is to find the longest consecutive repeat, 
  as well as change the return_val value.
  """

  for key in longest_dict:
    if longest_dict[key] == return_val:
      list.append(key)
          
  return list

  """
  In the for loop above, the code checks to see if the return_val is the same as the key count. Once
  it finishes checking, it then modifies the list from way earlier.
  """


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
