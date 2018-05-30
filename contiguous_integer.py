#https://practice.geeksforgeeks.org/problems/check-if-array-contains-contiguous-integers-with-duplicates-allowed/0
t = int(input().strip())
while t > 0:
    t = t - 1
    s = int(input().strip())
    arr = input().strip().split(" ")
    mx = 0
    mn = 1000001
    for i in arr:
        v = int(i)
        if mx < v:
            mx = v
        if mn > v:
            mn = v
    
    lookup = [0 for i in range(mx - mn + 1)]
    for i in arr:
        v = int(i)
        lookup[v - mn] = 1
        
    flag = 0
    for i in lookup:
        if i == 0:
            print("No")
            flag = 1
            break
        
    if flag == 0:
        print("Yes")
        
        
