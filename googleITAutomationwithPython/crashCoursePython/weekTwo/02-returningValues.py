# functions that sum two areas
def areaTriangle(base, heigth):
    return (base*heigth)/2

area_a = areaTriangle(7,4)
area_b = areaTriangle(6,2)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))
print("The sum of both areas is: ", sum)

# Create a function
name = "Kay"
num = len(name) * 9
print("Hello " + name + ". Your lucky number is " + str(num))

name = "Cameron"
num = len(name) * 9
print("Hello " + name + ". Your lucky number is " + str(num))

def num_lucky(name):
    number = len(name) * 9
    print("Hello " + name + ".  Your lucky number is " + str(number))

num_lucky("Kay")
num_lucky("Cameron")


