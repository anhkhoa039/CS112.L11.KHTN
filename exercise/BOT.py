n =16
l = [2,-4,5,-8,4,-1,-1,1,1,1,-2,2,4,-6,9,-4]

# cách 1
def f(n,l):
    s= 0
    for i in range(n):
        s= s + l[i]
    return s
def bot (n,l):
    s = -10e18
    a,b = -1,-1
    for p in range (n-1):
        for q in range (p+1,n):
            if f(q,l)- f(p,l) > s:
                s = f(q,l)- f(p,l)
                a,b= p+1,q

    return s, a,b
s, p,q = bot (n,l)
print (p,q,s)    

#result: 5 15 12

# cách 2

def BOT():
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    maxsum = 0
    sum = a[0]
    star = 1
    end = 1
    for i in range(0, n):
        sum += a[i]
        if (sum < 0):
            sum = 0
            star = i + 2
        if(maxsum <= sum):
            maxsum = sum
            end = i + 1
    print(star, end, maxsum)
BOT()
