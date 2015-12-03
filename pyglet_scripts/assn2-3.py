# This first line is provided for you

hrs = raw_input("Enter Hours:\n")

# Let's create a variable for the hourly rate of pay

rate = raw_input("Enter rate of pay:\n")

""" Let's determine gross pay by turning strings into numbers and multiplaying
the hours worked by the hourly rate of pay
"""
gross_pay = float(rate) * int(hrs)

# Let's print the result from the user input

print gross_pay
