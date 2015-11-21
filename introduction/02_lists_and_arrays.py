# Introductory script. The most important python expressions and operations.
# Part 02 - Lists and Arrays
# author: Mikolaj Buchwald


############################################
#                                          #
#           LISTS AND ARRAYS               #
#                                          #
############################################

################################
#       list management        #
################################

# create list
a = [5, 2, 8, 3, 9]
a
# out: [5, 2, 8, 3, 9]

# list indices (indexes)
a[0]
# out: 5
a[2]
# out: 8

# length of the list:
len(a)
# out: 5

# ### get last element of the list (2 ways)
# way 1:
a[len(a)-1]
# out: 9

# way 2 (more pythonish):
a[-1]
# out: 9

# get 2nd to 5th element of the list
a[2:5]
# out: [8, 3, 9]


'''
Exercise 02.00
    Create list [6, 4, 9, 0, 5] and check its length.

Exercise 02.01
    Check what is the last element of the list created in exercise 02.00
    (in both ways).

Exercise 02.02
    Get 2nd to 4th elemnts of the list (counting from 0).

'''


################################
#    basic list operations     #
################################

# create a list
b = [0, 4, 2, 1, 1, 7]

# get maximal value of the list
max(a)
# out: 7

# as well as minimal
min(a)
# out: 0

# sum up elements
sum(b)
# out: 15 

# append element to the list
b.append(9)
b
# out: [0, 4, 2, 1, 1, 7, 9]

# pop element from the list (revese append)
b.pop()
# out: 9

b
# out: [0, 4, 2, 1, 1, 7]

b.pop()
# out: 7

b
# out: [0, 4, 2, 1, 1]

# you can pop n'th element by specifying pop() function argument
b.pop(0)
# out: 0

b
# out: [4, 2, 1, 1]

b.pop(0)
# out: 4

b
# out: [2, 1, 1]

# ### add two lists and how does it differ from append()
c = [8, 4, 7]

# add
b + c
# out: [2, 1, 1, 8, 4, 7]

# append
b.append(c)

b
# out: [2, 1, 1, [8, 4, 7]]

# ### list inside list issue
# python list can store almost all kind of python objects including lists

# sorting list
c.sort()
c
# out: [4, 7, 8]


'''
Exercise 02.03
    Sort list [6, 4, 9, 0, 5].

Exercise 02.04
    Append integer 1 to the sorted list from previous exercise.
    Then sort it again.
'''

################################
#            tuples            #
################################
# Python tuples are like lists but they are immutable. It is sometines useful.
# For more information see the discussion at:
# http://stackoverflow.com/questions/2174124/why-do-we-need-tuples-in-python-or-any-immutable-data-type

# What does immuutability mean?
# You can not append, pop nor change values of the tuple.
# Yet, you can still get elements from tuple by indices and obviously
# store data in it. 


################################
#        numpy arrays          #
################################

# ### create numpy array
import numpy as np

# numpy is python package for numeric operation
# It simulates C or JAVA-like arrays but is way more powerful in means of
# simple and quick arithmetic operations as well as matrix support,
# compatibility with many python packages for statistics,
# machine learning, etc.

d = np.array([4, 6, 2, 1, 6, 7, 9, 2])

# ### and now it is simple to get:

# max
d.max()
# out: 9

# max
d.min()
# out: 1

# sum
d.sum()
# out: 37

# product
d.prod()
# out: 36288

# mean
d.mean()
# out: 4.625

# variance
d.var()
# out: 6.984375

# standard deviation
d.std()
# out: 2.6427968139832467

# sort data
d.sort()
d
# out: array([1, 2, 2, 4, 6, 6, 7, 9])

'''
Exercise 02.05
    Create array [0.12, 0.55, 0.32, 0.9, -0.21].

    Then get it's:
        * maximal and minimal values,
        * sum,
        * product,
        * mean,
        * variance,
        * standard deviation,

   Sort the array.
'''
