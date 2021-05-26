# Task
# Complete the code in the editor below. The variables i, d, and s are already declared and initialized for you. You must declare
# variables: one of type int, one of type double, and one of type String. Then you must read 3 lines of input from stdin and initialize
# your variables. Finally, you must use the + operator to perform the following operations:

# Print the sum of i plus your int variable on a new line.
# Print the sum of d plus your double variable to a scale of one decimal place on a new line.
# Concatenate s with the string you read as input and print the result on a new line.
# Note: If you are using a language that doesn't support using + for string concatenation (e.g.: C), you can just print one variable
# immediately following the other on the same line. The string provided in your editor must be printed first, immediately followed by the
# string you read as input.

# Input Format
# The first line contains an integer, i.
# The second line contains a double, d.
# The third line contains a string, s.

# Output Format
# Print the sum of both integers on the first line, the sum of both doubles (scaled to 1 decimal place) on the second line, and then the
# two concatenated strings on the third line.

i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
i1=int(input())
d1=float(input())
s1=input()

# Print the sum of both variables on a new line.
print(i+i1)
print ("{0:.1f}".format(d+d1))
print(s+s1)

