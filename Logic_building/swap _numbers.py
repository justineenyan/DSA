
#Given two numbers a and b, write a program to swap them.

#Naive approach using a temporary variable
def swap_numbers(a, b):
    temp = a
    a = b
    b = temp
    return a, b

#Without using a temporary variable
if __name__ == "__main__":
    a = 5
    b = 10
    a = a + b
    b = a - b
    a = a - b
    print(a, b)

#Using tuple unpacking in Python
if __name__ == "__main__":
    a = 5
    b = 10
    a, b = b, a
    print(a, b)

#Using XOR operator
if __name__ == "__main__":
    a = 5
    b = 10
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(a, b)