# We need a simple function that determines if a plural is needed or not.
# It should take a number, and return true if a plural should be used with that number or false if not.
# This would be useful when printing out a string such as 5 minutes, 14 apples, or 1 sun.
#
# All values will be positive integers or floats, or zero.

def plural(n):
        return n != 1


### TEST CASES ###

# test case 1
print(plural(0))
# result: True

# test case 2
print(plural(0.5))
# result: True

# test case 3
print(plural(1))
# result: False

# test case 4
print(plural(100))
# result: True
