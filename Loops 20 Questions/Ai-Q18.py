# Use a loop to print numbers in reverse order within a given range.
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

for num in range(end, start - 1, -1):
    print(num)
