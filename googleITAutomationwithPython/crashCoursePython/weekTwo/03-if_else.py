# To evaluate as true, the (and) operator would need both expression to be true at the same time
print("Yellow" > "Cyan" and "Brown" > "Magenta")

# If we use the (or) operator, instead, the expression will be true if either of the expressions are true,
# and false only when both expression are false
print("Yellow" > "Cyan" or "Brown" > "Magenta")
print(25 > 50 or 1 != 2)

# The (not) operator inverts the value of the expression that's in front of it
print(not "Answer" == "Answer")
print(not 42 == "Answer")

# functions with if and else
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters  long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters  long")
    else:
        print("Valid username")

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

num = is_even(65)
print(num)
