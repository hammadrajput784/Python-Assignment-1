# User se input lena aur usay integer mein convert karna

num = int(input("Enter your number: "))
count = 0
while num != 0:
   count += 1
   num //= 10
print("Total digits:", count)
