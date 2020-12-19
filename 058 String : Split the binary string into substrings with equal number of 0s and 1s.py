
s=input()
ans=0
c=0
for i in s:
    if i=="0":
        c-=1
    else:
        c+=1
    if c==0:
        ans+=1
print(ans)





def maxSubStr(str, n): 
	count0 = 0
	count1 = 0
	cnt = 0
	
	for i in range(n): 
		if str[i] == '0': 
			count0 += 1
		else: 
			count1 += 1
			
		if count0 == count1: 
			cnt += 1

	if count0 != count1: 
		return -1
			
	return cnt 

str = "0100110101"
n = len(str) 
print(maxSubStr(str, n)) 
