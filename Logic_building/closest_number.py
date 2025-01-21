
#Given two integers n and m, find the number closest to n and divisible by m.
#where m is not equal to zero.
#If there are two such numbers, choose the absolute maximum number.
13, 4
def closestNumber(n, m):
    #find the quotient
    q  = int(n / m)

    # 1st possible closest number
    n1 = m * q

    # 2nd possible closest number
    if ((n * m) > 0):
        n2 = (m * (q + 1))
    else:
        n2 = (m * (q - 1))

    #if true, then n1 is the closest number
    if (abs(n - n1) < abs(n - n2)):
        return n1
    else:
        return n2


if __name__ == "__main__":
    n = 13
    m = 4
    print(closestNumber(n, m))