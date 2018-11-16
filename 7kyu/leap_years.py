# In this kata you should simply determine, whether a given year is a leap year or not.
# In case you don't know the rules, here they are:
#
#     years divisible by 4 are leap years
#     but years divisible by 100 are no leap years
#     but years divisible by 400 are leap years
#
# Additional Notes:
#     Only valid years (positive integers) will be tested, so you don't have to validate them
#
# Examples can be found in the test fixture.

def isLeapYear(year):
    return year % 100 != 0 and year % 4 == 0 or year % 400 == 0


### TEST CASES ###

# test case 1
print(isLeapYear(1984))
# result: True

# test case 2
print(isLeapYear(2000))
# result: True

# test case 3
print(isLeapYear(1234))
# result: False

# test case 4
print(isLeapYear(1100))
# result: False
