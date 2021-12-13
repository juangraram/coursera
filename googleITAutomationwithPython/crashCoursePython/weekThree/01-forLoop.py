# Example for
for x in range(5):
    print(x)

# Go through a list
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print('Hi ' + friend)

# Example for
product = 1
for n in range(1, 10):
    product = product * n

print(product)

# Convert celsius
def to_celsius(x):
    return (x-32)*5/9
# Iterate from 0 to 101 of 10 in 10
for x in range(0,101,10):
    print(x, to_celsius(x))