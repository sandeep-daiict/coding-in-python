t = int(raw_input())
twos = [1]

for i in range(1, 40):
    twos.append(2 * twos[i-1])

def nearest_difference(num):
    i = 0
    while(num > twos[i]):
        i = i + 1

    return (i, twos[i] - num)

while(t):
    t = t - 1
    x = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())
    arr = []
    for i in range(0,x):
        if i == 0:
            arr.append(0)
        if i == 1:
            arr.append(a)
        else:
            if i % 2 ==0:
                temp = min(arr[i-1] + a, arr[i/2] + b)
            else:
                temp = arr[i-1]
                n = nearest_difference(i)
            arr.append(min(temp, a * n[0] + b * n[1])
