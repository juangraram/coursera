# Example Basic String Methods
name = "Juan"
color = 'gold'
pet = "Tony"

res = name + color + pet * 3
print(res)
print(len(res))

# Example String Indexing and Slicing
nameOne = "Jaylen"
print(nameOne[1])
print(nameOne[4])
print(nameOne[-1])

colorOne = "Orange"
print(colorOne[1:4])
fruit = "Pineapple"
print(fruit[:4])
print(fruit[4:])

pets = "cats & dogs"
print(pets.index("&"))
print(pets.index("c"))

# Using the format() method
example = "format() method"
formatted_string = "this is an example of using then {} on a string".format(example)
print(formatted_string)

# "{0} {1}".format(first, second)
first = "apple"
second = "banana"
third = "carrot"
formatted_string = "{0} {2} {1}".format(first, second, third)
print(formatted_string)


# {:d} integer value
number = 10.5
print('{:.2f}'.format(number))

# Replace domain
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

one = replace_domain("juan@tech.com", "tech.com", "fertech.com")
print(one)

# String methods
print("Mountains".upper())
print("Mountains".lower())

answer = "YES"
if answer.lower() == "yes":
    print("User said yes")

# Strip method
print(" yes ".strip())

# lstrip method
print(" yes ".lstrip())

# rstrip method
print(" yes ".rstrip())

# count method
print("The number of times e occurs in this string is ".count("n"))

# endswith method
print("Forest".endswith("rest"))

# isnumeric method
print("Forest".isnumeric())

# join method
print("...".join(["This", "is", "phrase"]))

# split method
print("This is another example".split())

nombre = "Manny"
numberThree = len(nombre) * 3
print("Hello {}, your lucky number is {}".format(nombre, numberThree))
print(f"Your lucky number is {numberThree}, {nombre}.".format(nombre=nombre, numberThree=len(nombre)*3))

price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With tax: ${:.2f}".format(price, with_tax))