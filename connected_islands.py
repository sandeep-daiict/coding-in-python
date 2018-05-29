{
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[1])]for j in range(n[0])]
        c=0
        for i in range(n[0]):
            for j in range(n[1]):
                matrix[i][j] = arr[c]
                c+=1
        print(findIslands(matrix, n[0], n[1]))
# Contrubuted By: Harshit Sidhwa

}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# your task is to complete this function
# Your function should return an integer
def setFullIslandsZero(arr,i,j,n,m):
    if i<0 or j<0 or i>=n or j>=m or arr[i][j]==0 :
        return
    arr[i][j] = 0
    setFullIslandsZero(arr,i+1,j+1,n,m)
    setFullIslandsZero(arr,i+1,j,n,m)
    setFullIslandsZero(arr,i+1,j-1,n,m)
    setFullIslandsZero(arr,i,j+1,n,m)
    setFullIslandsZero(arr,i,j-1,n,m)
    setFullIslandsZero(arr,i-1,j+1,n,m)
    setFullIslandsZero(arr,i-1,j,n,m)
    setFullIslandsZero(arr,i-1,j-1,n,m)
    
    
def findIslands(arr, n, m):
    # Code here
    count = 0
    for i in range(0,n):
        for j in range(0,m):
            if arr[i][j] == 1:
                count = count + 1
                setFullIslandsZero(arr,i,j,n,m);
            else:
                continue;
    return count
