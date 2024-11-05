# Write a program that breaks 
# the loop when a certain condition is met.
while True:  
    number = int(input("Enter a number (0 to stop): "))  
    if number == 0: 
        print("Loop is broken.")
        break 
    print("You entered:", number)  
