n, m = map(int, input().split())
parent = [i for i in range (n)]
rank= [1]*n

def findset (x):
    if parent[x] == x:
        return x
    else:
        result = findset(parent[x])

        parent[x] = result
    return result
def union (x, y):

    xset = findset(x)
    yset = findset(y)

    if xset == yset:
        return 
    if rank[xset] < rank[yset]:
        parent[xset] = yset
    elif rank[xset] > rank[yset]:
        parent[yset] =  xset
    else:
        parent[yset] = xset
        rank[xset] = rank[xset] + 1

for i in range (m):
    a, b = map(int,input().split())
    union(a,b)

a = set(parent)
s = 1
module = 10**9+7
print (len(a)-1)
for i in a:
    # b.append(parent.count(i))
    s = s* parent.count(i)
print (s%module)

