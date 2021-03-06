# Introductory script. The most important python expressions and operations.
# Part 00 - Variables
# author: Mikolaj Buchwald


############################################
#                                          #
#              VARIABLES                   #
#                                          #
############################################

################################
#           variable           #
################################
a = 5

################################
#      types of variables      #
################################

# string variable
b = "t"
c = "cognitive computing"

# float variable
d = 25.8

# boolean variable
e = True

# type() function
type(a)
# out: int
type(b)
# out: string
type(c)
# out: string
type(d)
# out: float
type(e)
# out: bool

################################
#    variables constructors    #
################################

# int(), float(), str()
int('37')
# out: 37
type('37')
# out: str
type(int('37'))
# out: int

float(2)
# out: 2.0
float(a)
# out: 5.0

str(0.12)
# out: '0.12'

################################
#          exercises           #
################################
'''
Exercise 00.00
    Create 4 variables, one of each type: int, float, bool, str

Exercise 00.01
    You have given variable a=42.21
    Change variable type to str
'''
