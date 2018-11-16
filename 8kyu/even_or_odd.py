# Create a function (or write a script in Shell) that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
  if number % 2 == 0:
      return 'Even'
  return 'Odd'


### TEST CASES ###

# test case 1
print(even_or_odd(2))
# result: 'Even'

# test case 2
print(even_or_odd(0))
# result: 'Even'

# test case 3
print(even_or_odd(7))
# result: 'Odd'

# test case 4
print(even_or_odd(1))
# result: 'Odd'
