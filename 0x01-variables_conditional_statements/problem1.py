#! /usr/bin/python3

# Problem: Receive miles and convert to kilometers
# kilometers = miles * 1.60934
# Enter Miles 5
# 5 miles equals 8.04 kilometers

# Solution

# Ask the user to input miles and assign it ti the miles variable
miles = input('Enter Miles: ')

# Convert miles to Integer
miles = int(miles)

# Perform calcualtion by multiplying 1,60934 times miles
kilometers = miles * 1.60934

# Print results using format()
print("{} miles equals {} kilometers".format(miles, kilometers))
