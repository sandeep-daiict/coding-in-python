#code
t = int(input())
while t > 0:
    t = t - 1
    num = int(input())
    arr = []
    arr.append(1)
    arr.append(2)
    arr.append(4)
    if num<3:
        print(arr[num-1])
    else:
        for i in range(3,num):
            arr.append(arr[i-1] + arr[i-2] + arr[i-3])
        print(arr[-1])
