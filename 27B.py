from math import dist
with open('/home/student/Downloads/27_B_28766.txt') as file:
    f=file.readlines()
a=[]
for i in f:
    a.append(i.replace(',', '.').split())
    a[-1]=((float(a[-1][0]),float(a[-1][1])),(a[-1][2][0],int(a[-1][2][1]),a[-1][2][2:]))
def c(k):
    t=0
    mn=10**100
    for t1 in k:
        d=sum([dist(t1[0],t2[0]) for t2 in k])
        if d<mn:
            mn=d
            t=t1
    return t
def g(k):
    mn=10**100
    for t1 in k:
        for t2 in k:
            if dist(t1[0],t2[0])!=0:
                mn =min(mn,dist(t1[0],t2[0]))
    return mn
k1=[]
k2=[]
k3=[]
for i in a:
    if i[0][1]<15:
        k1.append(i)
    elif i[0][1]<23:
        k2.append(i)
    else:
        k3.append(i)
c1=c(k1)
c2=c(k2)
c3=c(k3)
k1=[t for t in k1 if t[1][0]=='Z'and t[1][2]=='I']
k2=[t for t in k2 if t[1][0]=='Z'and t[1][2]=='I']
k3=[t for t in k3 if t[1][0]=='Z'and t[1][2]=='I']
print(min([g(k1),g(k2),g(k3)])*10000,dist(c1[0],c2[0])*10000)