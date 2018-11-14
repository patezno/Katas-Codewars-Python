# Your function takes two arguments:
#
# 1. current father's age (years)
# 2. current age of his son (years)
#
# Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).

def twice_as_old(dad_years_old, son_years_old):
    twice_son = son_years_old * 2
    if twice_son > dad_years_old:
        return twice_son - dad_years_old
    if twice_son < dad_years_old:
        return dad_years_old - twice_son
    if twice_son == dad_years_old:
        return 0

### TEST CASES ###

# test case 1
print(twice_as_old(36, 7))
# result: 22

# test case 2
print(twice_as_old(55, 30))
# result: 5

# test case 3
print(twice_as_old(42, 21))
# result: 0

# test case 4
print(twice_as_old(22, 1))
# result: 20

# test case 5
print(twice_as_old(29, 0))
# result: 29
