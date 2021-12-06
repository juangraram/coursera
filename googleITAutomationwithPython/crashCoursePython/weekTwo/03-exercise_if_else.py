# Fill in the blanks, so the print statement displays the result of the function call in order.
#Hint: if a function returns multiple values, don't forget to store these values in multiple variables
# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
    if number2 > number1:
        return number1, number2
    else:
        return number2, number1

# Fill in the blanks so the print statement displays the result of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

# The is_positive function should return True if the number received is positive, otherwise it returns None.
def is_positive(number):
    if number > 0:
        return True
    else:
        return None

age = is_positive(-5)
print(age)

# The number_group function should return "Positive" if the number received is positive,
# "Negative" if it's negative, and "Zero" if it's 0.
def number_group(number):
  if number > 0:
    return "Positive"
  elif number < 0:
    return "Negative"
  else:
    return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative

# The function receives a name, then returns a greeting based on whether or not that name is "Taylor".
def greeting(name):
  if name == "Taylor":
    return "Welcome back, " + name
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))

# If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still
# use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this,
# calculate_storage function below, which calculates the total number of bytes needed to store a file of a given size?
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size * (full_blocks +1)
    return full_blocks * block_size


print(calculate_storage(1))  # Should be 4096
print(calculate_storage(4096))  # Should be 4096
print(calculate_storage(4097))  # Should be 8192
print(calculate_storage(6000))  # Should be 8192

# The color_translator function receives the name of a color, then prints its hexadecimal value. Currently,
# it only supports the three additive primary colors (red, green, blue), so it returns "unknown" for all other colors.
def color_translator(color):
    if color == "red":
        hex_color = "#ff0000"
    elif color == "green":
        hex_color = "#00ff00"
    elif color == "blue":
        hex_color = "#0000ff"
    else:
        hex_color = "unknown"
    return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown

# Students in a class receive their grades as Pass/Fail. Scores of 60 or more (out of 100) mean that the grade
# is "Pass". For lower scores, the grade is "Fail". In addition, scores above 95 (not included) are graded as
# "Top Score". Fill in this function so that it returns the proper grade.
def exam_grade(score):
	if score > 95:
		grade = "Top Score"
	elif score >= 60:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail

# This function receives the first_name and last_name parameters and then returns a properly formatted string.
# If both the last_name and the first_name parameters are supplied, the function should return like so
# print(format_name("Ella", "Fitzgerald"))
# Name: Fitzgerald, Ella
def format_name(first_name, last_name):
    if last_name != "" and first_name != "":
        return ("Name: " + last_name + ", " + first_name)
    elif first_name != "" or last_name != "":
        return ("Name: " + last_name + first_name)
    else:
        return ""


print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"
print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"
print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"
print(format_name("", ""))
# Should return an empty string


# The longest_word function is used to compare 3 words. It should return the word with the most number of characters
# (and the first in the list when they have the same length).
def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word1) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return (word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))

# The fractional_part function divides the numerator by the denominator, and returns just the fractional part
# (a number between 0 and 1). Complete the body of the function so that it returns the right number.
# Note: Since division by 0 produces an error, if the denominator is 0, the function should return 0
# instead of attempting the division.
def fractional_part(numerator, denominator):
    # Operate with numerator and denominator to
    # keep just the fractional part of the quotient
    if denominator == 0:
        return 0 #raise Exception('Not possible')
    elif numerator == 0:
        return 0
    # check if result of division is already smaller than 1
    if numerator < denominator:
       return numerator / denominator

    remainder  = numerator % denominator
    return remainder / denominator

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0