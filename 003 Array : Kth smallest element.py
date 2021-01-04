#https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1
def kthSmallest(arr, l, r, k):
    '''
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find k  th smallest element and return using this function
    '''
    arr.sort()
    return arr[k-1]
