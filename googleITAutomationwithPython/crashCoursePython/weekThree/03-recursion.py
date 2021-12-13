# recursion
def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
        return 1
    return n * factorial(n-1)

result = factorial(8)
print(result)

