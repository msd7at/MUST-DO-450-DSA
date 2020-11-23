#https://practice.geeksforgeeks.org/problems/count-element-occurences/1#
def countOccurence(arr,n,k):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    ans=0
    nk=n//k
    # print(d)
    for i in d:
        # print(i,math.ceil(n/d[i]))
        if d[i]>nk:
            ans+=1
    return ans
