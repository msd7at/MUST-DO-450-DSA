#https://www.geeksforgeeks.org/median-of-two-sorted-arrays/
x=list(map(int,input().split()))
y=list(map(int,input().split()))

def merge(x,y):
    m,n=len(x),len(y)
    for i in range(m):
        if y[0]<x[i]:
            x[i],y[0]=y[0],x[i]
            f=y[0]
            k=1
            while k<n and f>y[k]:
                y[k-1]=y[k]
                k+=1
            y[k-1]=f
merge(x,y)
print(x,y)
print("MEDIAN is ",(x[-1]+y[0])/2)
