# Write a program to calculate the sum of all numbers between 1 and 100.
# Initialize sum variable to store the total sum


sum=0
for i in range(0,101):
    sum+=i
    print(f"after adding {i}, the sum is: {sum}")