with open('D:/Users/Denis/Downloads/17_28762.txt') as f:
    f=f.readlines()
f=list(map(int,f))
mn=10**5
for i in f:
    if i%23==0:
        mn=min(mn,i)
k=[]
for i in range(len(f)-1):
    if f[i]%mn==0 or f[i+1]%mn==0:
        k.append(f[i+1]+f[i])
print(len(k),max(k))
