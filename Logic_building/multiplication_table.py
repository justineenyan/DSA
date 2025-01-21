#Program to print the multiplication table of a given number
n = int(input("Enter the number: "))
for i in range(1, 16):
    print(n, '*', i, '=', n * i)