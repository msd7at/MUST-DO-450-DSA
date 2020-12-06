#https://practice.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1#
def spirallyTraverse(matrix, r, c): 
    di=0
    top=0
    down=r-1
    left=0
    right=c-1
    jj=[]
    while left<=right and top<=down:
        if di==0:
            for i in range(left,right+1):
                # print(matrix[top][j],end=" ")
                jj.append(matrix[top][i])
            top+=1
        elif di==1:
            for i in range(top,down+1):
                # print(matrix[i][right],end=" ")
                jj.append(matrix[i][right])
            right-=1
        elif di==2:
            for i in range(right,left-1,-1):
                # print(matrix[down][j],end=" ")
                jj.append(matrix[down][i])
            down-=1
        else:
            for i in range(down,top-1,-1):
                # print(matrix[i][j],end=" ")
                jj.append(matrix[i][left])
            left+=1
        di=(di+1)%4
    # print(jj)
    return jj
