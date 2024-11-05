# Create a program to calculate the sum of the digits of an inputted integer.
# User se input lena
number = int(input("Enter an integer: "))


digit_sum = 0


while number > 0:
    digit_sum += number % 10  
    number //= 10 


print("Sum of the digits:", digit_sum)
