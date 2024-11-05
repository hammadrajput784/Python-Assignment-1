# Create a program that simulates a countdown timer starting from a given number down to zero.


import time

number = int(input("Enter a number to start the countdown: "))

for i in range(number, -1, -1):
    print(i)
    time.sleep(1)
