a= [[1,1],
    [1,0]]
b= [1,1]
modulo = 10**9+7
def mul_matrix (x,y):
    return [[(x[0][0] * y[0][0] + x[0][1] * y[1][0])% modulo,(x[0][0] * y[0][1] + x[0][1] * y[1][1])% modulo],
            [(x[1][0] * y[0][0] + x[1][1] * y[1][0])% modulo,(x[1][0] * y[0][1] + x[1][1] * y[1][1])% modulo]]
def mul_matrix1(x,y):
    return [
        (x[0][0] * y[0] + x[0][1] * y[1])% modulo,
        (x[1][0] * y[0] + x[1][1] * y[1])% modulo ]
def pow_matrix(n):
    if n==1:
        return a
    tmp = pow_matrix(n//2)

    if n%2 == 1:
        return mul_matrix( mul_matrix(tmp,tmp),a)
    else:
        return mul_matrix(tmp,tmp)
def fibo(n):
    return mul_matrix1(pow_matrix(n),b)[1]
n,k = map(int, input().split())
k *=2
res = fibo(k)
print ((n*res)%modulo)

#input: 3 2
#output: 15
