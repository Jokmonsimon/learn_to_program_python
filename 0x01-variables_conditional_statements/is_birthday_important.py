#! /usr/bin/python3

# We will provide different output based on age
# 1 - 18 -> Important
# 21, 50, > 65 -> Important
# All others -> Not Important
# Recieve age and store in age
# and : if both are true it returns true
# or: if either condition is true then true
#  not: Convert a true condition into a false
# if age is both greater than or equal to 1 and less than or equal to 18 - Important
# if age is either 21 or 50 - Important
# We check if age is less than 65 and then convert true to false and vice versa
# Else Not Important

age = eval(input('Enter age: '))

if (age >= 1) and (age <= 18):
    print("Important Birthday")
elif (age == 21) or (age == 50):
    print("Important Birthday")
elif not (age < 65):
    print("Important Birthday")
else:
    print("Sorry! Not Important")
