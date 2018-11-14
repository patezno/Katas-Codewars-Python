# Jenny has written a function that returns a greeting for a user.
# However, she's in love with Johnny, and would like to greet him slightly different.
# She added a special case to her function, but she made a mistake.
#
# Can you help her?

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


### TEST CASES ###

# test case 1
print(greet("James"))
# result: "Hello, James!"

# test case 2
print(greet("Jane"))
# result: "Hello, Jane!"

# test case 3
print(greet("Jim"))
# result: "Hello, Jim!"

# test case 4
print(greet("Johnny"))
# result: "Hello, my love!"
