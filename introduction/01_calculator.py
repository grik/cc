# Introductory script. The most important python expressions and operations.
# Part 01 - Calculator
# author: Mikolaj Buchwald


############################################
#                                          #
#              CALCULATOR                  #
#                                          #
############################################

################################
# basic arithmetic operations  #
################################

# addition
1 + 2
# out: 3

# subtraction
15 - 23
# out: -8

# multiplication
1.63 * 34
# out: 55.419999999999995

# division
205/5
# out: 41


# IMPORTANT remark on division! #
22/7
# out: 3
# something is not right!

22/7.0
# out: 3.142857142857143
# now it is all right

# useful shortcut
a = 3
a = a + 5
a
# out: 8

a = 3
a += 5
a
# out: 8


################################
#   perform some operations    #
################################


################################
#    Comparison Operatorsns    #
################################
# gives truth values as return (boolean type)

2 < 4
# out: True

0.2 > 52352.3123
# out: False

# IMPORTANT: the difference between:
#   an "Assignment Operator", represented by sign "="
#   a "Comparision Operator", represented by sign "=="
2 == 2
# out: True

3/4.0 == 25
# out: False

# There are also: ">=", "<="

type(67 < 23)
# out: bool

# useful operator: modulo "%" - reminder after division
4 % 2
# out: 0

12 % 5
# out: 2
# because 12==2*5+2, where +2 is our reminder

# usefulness of modulo: discriminate between even and odd numbers
# question: is the number even? Modulo it by 2. If reminder is 0 then
# number if even, else it is odd. Let's see:

#   Question: Is 5 even?
5 % 2 == 0
# out: False
#   Answer: No, it is not.

#   Question: Is 92342740 even?
92342740 % 2 == 0
# out: True
#   Answer: Yes, it is.


################################
#          exercises           #
################################
'''
Exercise 01.00
    Add 9382743 to 823463.

Exercise 01.01
    Divide 77 by 3 and multiply it by 98.

Exercise 01.02
    Assign value 67.5 to variable named "activation" and then compare it
    (using "is equal to" operator) to product of 12.5 times 5.4

Exercise 01.03
    Is 92721 divisible by 3?
'''
