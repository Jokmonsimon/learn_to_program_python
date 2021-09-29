#! /usr/bin/python3

# If age is 5 - Go to Kindergarten
# Ages 6 through 17 - goes to 1 through 12
# If age is greater than 17 - say go to college
# Try to complete with 10 or less lines

#Solution
# Ask for the age
# Handle if age < 5
# Special output just for age 5
# Since a number is the result for ages 6 - 17, we check them all with 1 condition
# Handle everyone else

age = eval(input("Enter age: "))

if (age < 5):
    print("Too Young for School")
elif (age == 5):
    print("Go to Kindergarten")
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to grade {}".format(grade))
else:
    print("Go to College")
