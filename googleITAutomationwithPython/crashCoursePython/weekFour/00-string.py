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
'{:d}'.format(10.5)