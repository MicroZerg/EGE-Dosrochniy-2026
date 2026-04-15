from math import dist
with open('/home/student/Downloads/27_A_28766.txt') as file:
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
k1=[]
k2=[]
for i in a:
    if i[0][1]>8:
        k1.append(i)
    else:
        k2.append(i)
print(len(k1),len(k2))
r=[dist(c(k1)[0],t[0]) for t in a if t[1][0]=='Y'and t[1][2]=='III']
print(min(r)*10000,max(r)*10000)