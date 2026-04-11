def p(n):
    k=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            k.append(i)
            k.append(n//i)
    return k
for i in range(700001,800001):
    b=[]
    b=[j for j in p(i) if str(j)[-1]=='7' and j!=7 and j!=i]
    if len(b)!=0:
        print(i,min(b))
            
