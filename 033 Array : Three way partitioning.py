#https://practice.geeksforgeeks.org/problems/three-way-partitioning/1#
class Solution:
	def threeWayPartition(self, array, a, b):
	    # code here 
        i=0
        e=len(array)-1
        st=0
        while i<=e:
            if array[i]<a:
                array[i],array[st]=array[st],array[i]
                i+=1
                st+=1
            elif array[i]>b:
                array[i],array[e]=array[e],array[i]
                e-=1
            else:
                i+=1
        return array
