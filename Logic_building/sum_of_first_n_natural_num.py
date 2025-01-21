#Naive approach with a time complexity of O(n) and space complexity of O(1)
n = int(input("Enter the number: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum of first", n, "natural numbers is", sum)

#Optimized approach with a time complexity of O(1) and space complexity of O(1)
n = int(input("Enter the number: "))
sum = n * (n + 1) // 2
print("Sum of first", n, "natural numbers is", sum)

#Efficient Python program to find sum 
#of first n natural numbers that avoids overflow

def findsum(n):
    if n % 2 == 0:
        return (n // 2) * (n + 1)
    else:
        return ((n + 1) // 2) * n