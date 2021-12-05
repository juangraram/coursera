# Use the get_seconds function to work out the amount of seconds in 2 hours and 30 minutes,
# then add this number to the amount of seconds in 45 minutes and 15 seconds.
# Then print the result.
def get_seconds(oneHour, oneMinute, seconds):
    return oneHour*3600 + oneMinute*60 + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a + amount_b
print(amount_a, amount_b)
print(result)

#  function called month_days, that receives thename of the month and the number of days in that month as parameters.
#  Adapt the rest of the code so that the result is the same. Confirm your results by making a function call with
#  the correct parameters for both months listed.
def month_days(month, days):
    print(month + " has " + str(days) + " days.")

month_days("June","30")
month_days("July","31")

# This function converts miles to kilometers (km). Complete the function to return the result of the conversion
# Call the function to convert the trip distance from miles to kilometers Fill in the blank to print the
# result of the conversion Calculate the round-trip in kilometers by doubling the result,
# and fill in the blank to print the result
# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

my_trip_miles = 55

# Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(20)

# Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# Calculate the round-trip in kilometers by doubling the result, and fill in the blank to print the result
print("The round-trip in kilometers is " + str(my_trip_km * 2))

# Let's revisit our lucky_number function. We want to change it, so that instead of printing the message,
# it returns the message. This way, the calling line can print the message, or do something else with it if needed.
# Fill in the blanks to complete the code to make it work.
def lucky_number(name):
    number = len(name) * 9
    result = "Hello " + name + ". Your lucky number is " + str(number)
    return result


print(lucky_number("Kay"))
print(lucky_number("Cameron"))
