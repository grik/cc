# Introductory script. The most important python expressions and operations.
# Part 05 - Scripts
# author: Mikolaj Buchwald


############################################
#                                          #
#                SCRIPTS                   #
#                                          #
############################################

################################
#  how does script look like   #
################################

cat 05_supplement_example_script.py
# sub_num = 1
# print('Now we consider subject number: %03d' % sub_num)


################################
#   2 ways to run the script   #
################################

# From bash shell:
# python 05_supplement_example_script.py

# From ipython shell:
run 05_supplement_example_script.py
# Now we consider subject number: 001

# We can run more complicated scripts
run 05_supplement_more_complex_script.py
# Sum of 5 and 8 is 13


'''
Exercise 04.00
    Create your own, simple script and run it from ipython as well as from
    bash shell. Use print function to present results of your script's work.
'''


################################
#     Function from script     #
################################

# run script in ipython
run 05_supplement_function_in_script.py

# now you can use our function
summation(4, 8)
# out: 12


'''
Exercise 04.01
    Create your own, script and run it from ipython as well as from
    bash shell. Use print function to present results of your script's work.
'''
