#With Extra Space

class Solution:
def totalMoney(self, n: int) -> int:
	l=[0]*7
	c=0
	for i in range(n):
		if i%7==0:
			l[0]=l[0]+1
			c=c+l[0]
		else:
			l[i%7]=l[(i%7)-1]+1
			c+=l[i%7]
	return c

#Without Extra Space

class Solution:
    def totalMoney(self, n: int) -> int:
        l=[0]*7
        c=0
        it=0
        for i in range(n):
            if i%7==0:
                it+=1
                cpt=it
                c=c+it
            else:
                cpt+=1
                c+=cpt
        return c
