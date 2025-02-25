# week 3 lab work
# convert.py file
# Fergus McTiernan

# I learned that using the decimal function is the best way to ensure accuracy in currency calculations rather than the float function
# due to the fact that the float function uses binary floating point arithmetic which can result in rounding errors
# I also learned that the decimal function can be used to set the precision and rounding method for the calculation

import decimal
from decimal import Decimal, getcontext, Context

# setting up the decimal function by passing keyword arguments using the context module/library
new_context = Context(prec=100, rounding=decimal.ROUND_DOWN)

# taking input from user using Decimal function to ensure accuracy in cent conversion
user_input = Decimal(input("Enter amount in dollars: "))

# ensuring value is positive
user_input = abs(user_input)

#converting to cents
user_input = Decimal(user_input) * 100
user_input_int = int(user_input)

#printing result
print(f"Your amount in cents is {user_input}")
      




