
#Given an array of n integers.The task is to check whether
#an arithmetic progression can be formed using all the given elements.
#If possible print “YES” else print “NO”.

def checkIsAP(arr, n):
    m = {}
    smallest = float('inf')
    second_smallest = float('inf')


    for i in range(n):
        if arr[i] < smallest:
            second_smallest = smallest
            smallest = arr[i]

        elif arr[i] != smallest and arr[i] < second_smallest:
            second_smallest = arr[i]

        if arr[i] not in m:
            m[arr[i]] = 1

        else:
            return False

    diff = second_smallest - smallest

    current = smallest
    for i in range(n):
        if current not in m:
            return False
        current += diff

    return True


if __name__ == '__main__':
    arr = [1, 4, 7, 10, 13]
    n = len(arr)

    if checkIsAP(arr, n):
        print("YES")
    else:
        print("NO")  