# Create a program that evaluates if an inputted number is prime.
num=int(input("Enter your number :"))
if num<2:
    print(f"{num} is not a prime number.")
else:
    for i in range (2,num):
        if num%i==0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is primer number")