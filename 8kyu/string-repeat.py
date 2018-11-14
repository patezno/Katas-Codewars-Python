# Write a function called repeatStr which repeats the given string string exactly n times.

def repeat_str(repeat, string):
    return repeat * string

### TEST CASES ###

# test case 1
print(repeat_str(4, 'a'))
# result: 'aaaa'

# test case 2
print(repeat_str(3, 'hello '))
# result: 'hello hello hello '

# test case 3
print(repeat_str(2, 'abc'))
# result: 'abcabc'
