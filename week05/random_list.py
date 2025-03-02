# This was a real struggle
# Weekly lab 05
# Randomly generates a list of 10 intergers and loops through the list stating and then removing the first interger in the list each time
# Fergus McTiernan

import random

queue = []

for i in range (10):
    i = random.randint(1, 100)
    queue.append(i)
    
print(f"The numbers in the queue are {queue}")

for q in queue[0:10]:
    print(f"The current number is {queue.pop(0)}. The numbers remaining in the queue are {queue}")
    if queue == []:
        print("The queue is now empty.")

