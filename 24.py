from re import findall
with open('D:/Users/Denis/Downloads/24_28765.txt') as file:
    f=file.readline()
L=-1
R=-1
c=0
mx=0
while True:
    if c<=180:
        R+=1
        if len(f)<R:
            break
        if f[R-1:R+1]=='BC':
            c+=1
    else:
        L+=1
        if len(f)<L:
            break
        if f[L-1:L+1]=='BC':
            c-=1
    if c<=180 and (R-L+1)>mx:
        mx=R-L+1
print(mx)
