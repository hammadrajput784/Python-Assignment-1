# Find the factorial of a number using a while loop.
num=float(input("Enter your number :"))
factorial=1
while num>1:
    factorial*=num
    num-=1
print("Factorial is :",factorial)