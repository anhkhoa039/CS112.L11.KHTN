from math import *
a = int(input())
b = int(input())
c = int(input())
d = int(input())
def rutgon(a ,b):
    n = gcd(a ,b)
    return (a//n), (b//n)

def BienDoi(a, b, c, d):
    temp = 0
    while not (a == c and b == d) or (a/b > c/d):
        a, b = rutgon(a + 1, b + 1)
        temp += 1
        if a/b > c/d:
            return 0
    return temp

print(BienDoi(a, b, c, d))