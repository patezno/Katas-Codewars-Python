# A hero is on his way to the castle to complete his mission.
# However, he's been told that the castle is surrounded with a couple of powerful dragons!
# each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry..
# Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?
#
# Return True if yes, False otherwise :)

def hero(bullets, dragons):
    if bullets >= dragons * 2:
        return True
    else:
        return False


### TEST CASES ###

# test case 1
print(hero(10, 5))
# result: True

# test case 2
print(hero(7, 4))
# result: False

# test case 3
print(hero(4, 5))
# result: False

# test case 4
print(hero(100, 40))
# result: True

# test case 5
print(hero(1500, 751))
# result: False

# test case 6
print(hero(0, 1))
# result: False
