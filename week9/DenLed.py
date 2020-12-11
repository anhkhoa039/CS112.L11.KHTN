n = int(input())

if n % 3 == 0:
    Sum = (n // 3)*7
elif n % 3 == 1:
    Sum = (n // 3 - 1)*7 + 4
else:
    Sum = (n//3)*7 + 1
print(Sum)
