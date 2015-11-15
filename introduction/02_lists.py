# Introductory script. The most important python expressions and operations.
# Part 02 - Lists
# author: Mikolaj Buchwald


############################################
#                                          #
#                LISTS                     #
#                                          #
############################################

# list creation
a = [5, 2, 8, 3, 9]
a
# out: [5, 2, 8]

# list indices (indexes)
a[0]
# out: 5
a[2]
# out: 8

# length of the list:
len(a)
# out: 5

# get last element of the list (2 ways)
# way 1:
a[len(a)-1]
# out: 8

# way 2 (more pythonish):
a[-1]
# out: 8
