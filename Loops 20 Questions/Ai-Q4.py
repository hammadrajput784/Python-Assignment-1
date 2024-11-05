# Print the multiplication table of a given number.


num=float(input("Enter your number :"))

sum=0
while sum<=10:
    result=num*sum
    print(f"{num}*{sum}={result}")

    sum+=1
