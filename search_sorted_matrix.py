#code
#https://practice.geeksforgeeks.org/problems/search-in-a-matrix/0
t = int(input())
while t > 0:
    t = t - 1
    val = input().strip().split(" ")
    
    n,m = int(val[0]),int(val[1])
    val = input().strip().split(" ")
    arr = [  [int(val[i]) for i in range(m*j, m*j + m)] for j in range(0,n)]
    
    k = int(input())
    i = 0
    j = m-1
    out = 0
    
    while i >= 0 and i < n and j >= 0 and j < m:
        
        if arr[i][j] == k:
            out = 1    
            break
        elif arr[i][j] < k:
            i = i + 1
        elif arr[i][j] > k:
            j = j - 1
        
    
    print(out)
            
                
