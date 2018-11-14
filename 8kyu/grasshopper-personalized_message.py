# Create a function that gives a personalized greeting.
# This function takes two parameters: name and owner.
#
# Use conditionals to return the proper message.

def greet(name, owner):
    if name == owner:
        return 'Hello boss'
    return 'Hello guest'


### TEST CASES ###

# test case 1
print(greet('Daniel', 'Daniel'))
# result: 'Hello boss'

# test case 2
print(greet('Greg', 'Daniel'))
# result: 'Hello guest'
