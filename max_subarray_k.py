#https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
#code
t = int(input())
while t > 0:
    t = t - 1
    s = input().strip().split(" ")
    s,k = int(s[0]),int(s[1])
    arr = [int(i) for i in input().strip().split(" ")]
    maximum_local = 0
    last_max_index = 0
    for i in range(0,s):
        if i < k:
           if arr[i]  > maximum_local:
               maximum_local = arr[i]
               last_max_index = i
        else:
            print(maximum_local, end=" ")
            if arr[i]  > maximum_local:
               maximum_local = arr[i]
               last_max_index = i
            else:
                if i - last_max_index >= k:
                    last_max_index = last_max_index + 1
                    maximum_local = arr[last_max_index]
                    j = last_max_index
                    while j <= i:
                        if arr[j]>maximum_local:
                            maximum_local = arr[j]
                            last_max_index = j
                        j = j + 1
    else:
        print(maximum_local)
                    
