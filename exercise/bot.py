

def BOT():
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    maxsum = -1000000000000000000
    sum = 0
    p = 1
    for i in range(0, n):
        sum += a[i]
        if (sum < 0):
            sum = 0
            p = i + 2
        if(maxsum < sum):
            maxsum = sum
            star = p
            end = i + 1
    print(star,end,maxsum,end=' ')
BOT()
