# Introductory script. The most important python expressions and operations.
# Part 04 - Functions
# author: Mikolaj Buchwald


############################################
#                                          #
#               FUNCTIONS                  #
#                                          #
############################################

################################
# short intro:                 #
# what the function really is? #
################################

# ### Definition 04.00:
# FUNCTION TAKES AN ARGUMENT AND RETURNS A VALUE!

# y is a linear function
def y(a, x, b):
    return a*x+b

'''
where:
    * a - slope (constant)
    * x - argument (variable)
    * b - intercept (constant)
'''

# generate a sequence <0, 49> len=50, but we start counting from 0
arguments = range(50)

# calculate the values by applying the function
a = 1
b = 0
values = [y(a, arguments[x], b) for x in arguments]  

# plot values for arguments
import matplotlib.pyplot as plt
plt.plot(arguments, values, 'o')
plt.xlabel('arguments of the function')
plt.ylabel('values of the function')
plt.show()

# try diffrent a's and b's

a, b = 2.5, 0
values_00 = [y(a, arguments[x], b) for x in arguments]  

a, b = 2.5, 15
values_01 = [y(a, arguments[x], b) for x in arguments]  

a, b = -1.2, 30
values_02 = [y(a, arguments[x], b) for x in arguments]  

plt.plot(arguments, values, 'b')
plt.plot(arguments, values_00, 'ro')
plt.plot(arguments, values_01, 'go')
plt.plot(arguments, values_02, 'bo')

plt.show()


'''
Exercise 04.00
    One of the simplests but at the same one of the most important exercises
    during this course:

        Repeat function definition (definition 04.00). Aloud.
        And do so each time next classes begins.
'''

################################
#    simple function example   #
################################

# define summation function
def summation(a, b):
    return a + b

summation(6, 3)
# out: 9

# notice, that it RETURNS some value - it means we can assign the value of the
# function to some variable, for example:

c = summation(8.6, 7.2)
c
# out: 15.8


'''
Exercise 04.01
    Create a subtraction function. And call it on some arguments.

Exercise 04.02
    Function that takes three arguments. Example. Your invention.
'''
