s1 = input()
s2= input()
dic = {}
count = 0

for i in range (len(s2) -1):
    x= s2[i:i+2]
    try :
        dic[x] += 1
    except:
        dic[x] = 1
for i in range (len (s1) -1):
    x = s1[i:i+2]

    if x  in dic:
        count += 1
print (count)