t = int(input())
while t>0:
    t = t - 1
    size = int(input())
    arr = str(raw_input()).split(" ")
    if size<3:

        print("-99999")
        continue
    a = int(arr[0])
    b = int(arr[1])
    c = int(arr[2])
    if a + b == c:
        print(int(arr[-1]) + int(arr[-2]))
        continue
    if c - b == b - a:
        print(int(arr[-1]) + b - a)
        continue
    if a != b and c != b and c/b == b/a:
        print(int(arr[-1]) * (b / a))
        continue
    print("-99999")

