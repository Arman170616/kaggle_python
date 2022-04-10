pi = 3.14159 # approximate
diameter = 3

# Create a variable called 'radius' equal to half the diameter
radius = diameter/2
print(radius)
# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared
area = pi * radius ** 2      # pi* r2

#Add code to the following cell to swap variables `a` and `b` (so that `a` refers to the object previously referred to by `b` and vice versa).

a = [1, 2, 3]
b = [3, 2, 1]

print(a)
print(b)
c = a
a = b
b = c
print(a)
print(b)

"""
The most straightforward solution is to use a third variable to temporarily store one of the old values. e.g.:

tmp = a
a = b
b = tmp
If you've read lots of Python code, you might have seen the following trick to swap two variables in one line:

a, b = b, a
We'll demystify this bit of Python magic later when we talk about tuples.
"""

#Add parentheses to the following expression so that it evaluates to 1.

a = (5 - 3) // 2
print(a)

#Hint: Following its default "BEDMAS"-like rules for order of operations, Python will first divide 3 by 2, then subtract the result from 5. You need to add parentheses to force it to perform the subtraction first



#Add parentheses to the following expression so that it evaluates to 0.

b = 8 - (3 * 2) - (1 + 1)
print(b)

'''
Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly among themselves. For the sake of their friendship, any candies left over will be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.

Write an arithmetic expression below to calculate how many candies they must smash for a given haul.

'''

# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109

# Your code goes here! Replace the right-hand side of this assignment with an expression
# involving alice_candies, bob_candies, and carol_candies
to_smash = -1
print((alice_candies + bob_candies + carol_candies) % 3)