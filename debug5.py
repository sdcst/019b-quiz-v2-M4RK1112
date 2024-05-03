#!python3
"""
Fix this program.
It should ask the user to enter in 10 numbers and see
if the number is positive or negative
"""
for n in (10):
    num = int(input("enter a number: "))
if num > 0:
    print('that is a positive number')
elif num < 0:
    print('that is a negative number')
else:
    print('zero is neither positive nor negative')
