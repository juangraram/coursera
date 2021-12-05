# Function so that it prints the total amount of seconds given the hours,
# minutes, and seconds function parameters. Remember that there are 3600 seconds in an hour and 60 seconds in a minute.
def print_seconds(oneHour, oneMinute, seconds):
    total_seconds = oneHour * 3600 + oneMinute * 60 + seconds
    print(total_seconds)

print_seconds(1, 2, 3)