t=int(input())
numbers=[]
for i in range(t):
    n=int(input())
    if n>=0 and n<1000:
        numbers.append(n)
fibb=[0,1]
for i in range (2,1000):
    m=fibb[i-1]+fibb[i-2]
    fibb.append(m)
for item in numbers:
    if item in fibb:
        print("YES")
    else:
        print("NO")