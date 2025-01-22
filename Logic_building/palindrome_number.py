
#Given an integer x, return true if x is a palindrome integer.
#An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

#Naive approach
def palindrome(number):
    num = str(abs(number))
    mid = len(num) // 2
    j = len(num) - 1
    for i in range(mid):
        if num[i] != num[j]:
            return False
        j -= 1
    return True

#Optimized approach
def is_palindrome(number):
    if number < 0 or(number % 10 == 0 and number != 0):
        return False
    
    reversed_half = 0
    while number > reversed_half:
        reversed_half = reversed_half * 10 + number % 10
        number //= 10

        if number == reversed_half or number == reversed_half // 10:
            return True

if __name__ == "__main__":
    print(is_palindrome(10))