# week 03 lab
# random fruit file
# Fergus McTiernan

import random

fruits = ['Apples', 'Orange', 'Banana', 'Pear']

index = random.randint(0, len(fruits)-1)

fruit = fruits[index]
print(f"Here is a random fruit: {fruit}")