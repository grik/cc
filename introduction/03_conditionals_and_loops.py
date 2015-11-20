# Introductory script. The most important python expressions and operations.
# Part 03 - Conditionals and Loops
# author: Maciej Malkowski


############################################
#                                          #
#         CONDITIONALS AND LOOPS           #
#                                          #
############################################

################################
#         conditionals         #
################################

# The three conditional statements are if, elif (else-if) and else

# The following checks whether the "if" statement is true and executes the
# indented block if it is. It does nothing otherwise:

grade = 3
if grade > 2:
    print "You pass!"
# out: "You pass!"
print
    
# The following checks whether the "if" statement is true and executes the first 
# indented block if it is. 

# Should the "if condition" be false, the "else" block is executed instead:

grade = 2
if grade > 2:
    print "You pass!"
else:
    print "You fail!"
# out: "You fail!"
print 
    
# Lastly, the following checks whether the "if" statement is true and executes the first
# indented block if it is. 

# If it's not, it checks every elif statement in succession and if it finds a true condition,
# it's corresponding code block is executed and no other else-if of else statements are checked. 

# If all "elifs" fail, then "else" is executed:

score = 75
if score == 100:
    print "Perfect!"
elif score > 90:
    print "Well done!"
elif score > 80:
    print "Not bad!"
elif score > 70:
    print "You did ok!"
elif score > 50:    
    print "You need some practice!"
else:
    print "Better luck next time!"
# out: "You did ok!"
print 

################################
#          Exercise 1          #
################################

# Think about this next block before running it. What is going to happen?
# Check your answer.
"""
score = 90
if score == 100:
    print "Perfect!"
if score > 90:
    print "Well done!"
if score > 80:
    print "Not bad!"
if score > 70:
    print "You did ok!"
if score > 50:    
    print "You need some practice!"
else:
    print "Better luck next time!"
# out: ?
print
"""
################################
#         the FOR  loop        #
################################

# The for loop does the listed instruction once for each item in an iterable,
# like a list or a tuple:

# Here for a list of strings:
friends = ["Mary", "Tommy", "Jackie", "Jimmy"]
for friend in friends:
    print "Hello", friend + "!"
print

# "friend" is a so-called dummy variable, because it's only used as a temporary
# placeholder.

# And for a tuple of integers:
numbers = (1, 2, 3, 4, 5)
for number in numbers:
    print number
print 

# For more interesting results, you can operate on those items:
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number
print sum    
# out: 15
print

# The same can be achieved with a very useful range() function:
print range(3)
print range(10)
print range(1, 10) 
print 

################################
#          Exercise 2          #
################################

# Recreate the above 'sum' loop using range(). You need 4 lines of 
# code.

################################
#          Exercise 3          #
################################
"""
# How many times will "practice" be printed here?

print "The secret to learning how to program is..."
for dummy_i in range(133):
    print "practice,"
print "practice!"    
"""
################################
#        the WHILE  loop       #
################################

# The while loop executes as long as the condition holds true:
i = 5
while i > 0:
    print i
    i -= 1
print "BOOM!"    
print     

import random

# Sometimes it's useful to have more control over where the loop
# stops. Remember that the condition is a boolean, so you can do the following:
secret_number = random.randrange(1, 21)
# random.randrange simply selects a pseudorandom number in range(1, 20)
# break statement exits the loop
while True:
    if secret_number == 1:
        print "The secret number was odd!"
        break
    if secret_number == 2:
        print "The secret number was even!"
        break
    secret_number -= 2    
print "We are out of the loop!"
print 
    
################################
#          Exercise 4          #
################################

# Suppose we were to change the random.randrange(1, 21) above to random.randrange(21).
# Why is that a bad idea?

################################
#          Exercise 5          #
################################

# 1) Examine the following code carefully and quess what it does. Run it to check your
# guess. See if you can stop it. 

# 2) Then modify it to take any non-empty string at all. Think before you run your program to 
# avoid being stuck in an infinite loop.
"""
letter=''

while letter!='q':
    letter = raw_input ()
    print('the letter you have chosen is: %s' % letter)
"""    
