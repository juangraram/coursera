# Example While Loop
x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    print("Not there yet, x=", x)
    x = x + 1
print("x=" + str(x))
print("x=", x)

# While loop inside of function
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")

attempts(5)

# while loops with two variables
x = 0
sum = 0
while x < 10:
    sum += x
    x += 1
    print(x, sum)

# Example while loops
def count_down(start_number):
    current = 5
    while current > 0:
        print(current)
        current -= 1
    print("Zero!")

count_down(3)

# Loop through the numbers from start to end
def print_range(start, end):
    n = start
    while n <= end:
        print(n)
        n += 1

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)
