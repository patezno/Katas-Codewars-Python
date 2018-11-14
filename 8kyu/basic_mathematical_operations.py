# Your task is to create a function that does four basic mathematical operations.
#
# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2

### TEST CASES ###

# test case 1
print(basic_op('+', 4, 7))
# result: 11

# test case 2
print(basic_op('-', 15, 18))
# result: -3

# test case 3
print(basic_op('*', 5, 5))
# result: 25

# test case 4
print(basic_op('/', 49, 7))
# result: 7
