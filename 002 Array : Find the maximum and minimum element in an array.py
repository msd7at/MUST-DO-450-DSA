#https://practice.geeksforgeeks.org/problems/middle-of-three2926/1#
class Solution:
    def middle(self,A,B,C):
        if (A<=B and A <=C and C>=A and C>=B) or (A>=B and A >=C and C<=A and C<=B)  :
            return B
        elif (B <= A and B <=C and C>=A and C>=B)or (B >= A and B >=C and C<=A and C<=B):
            return A
        else:
            return C
