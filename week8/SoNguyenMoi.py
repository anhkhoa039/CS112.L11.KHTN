n = int(input())

l = list(str(n))
x = 3 - n%3

Run = True
i = 0
while Run:
    p = int(l[i]) + x
    if (p < 10):
        while p < 7:
            p += 3
        l[i] = str(p)
        Run = False
    i += 1
    if i == len(l):
        Run = False

if "".join(l) != str(n):
    print("".join(l))
else:
    if n % 3 == 0:
        temp = int(l[-1]) - 3
    else:
        temp = int(l[-1]) - n%3
    l[-1] = str(temp)
    print("".join(l))
