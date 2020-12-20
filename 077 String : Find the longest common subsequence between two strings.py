#https://practice.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1#
#User function Template for python3
def lcs(m,n,X,Y):
    '''
    :param m: length of string X 
    :param n: length of string Y
    :param X: string X
    :param Y: string Y
    :return: Integer
    '''
    # code here
    l=[[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1]==Y[j-1]:
                l[i][j]=l[i-1][j-1]+1
            else:
                l[i][j]=max(l[i][j-1],l[i-1][j])
    return l[m][n]
                
