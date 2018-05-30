
def comp(a, b):
    k1,v1 = a
    k2,v2 = b
    if v1 > v2:
        return -1
    if v1<v2:
        return 1
    if k1>k2:
        return 1
    if k1<k2:
        return -1

def frequency_sort(arr):
    map = {}
    out = []
    for elem in arr:
        if elem in map:
            map[elem] = map[elem] + 1
        else:
            map[elem] = 1

    for key, value in sorted(map.iteritems(), cmp=comp):
        for i in range(value):
            out.append(key)
    return out

def main():
    test_case = int(raw_input())
    arr = []
    while test_case > 0:
        test_case = test_case - 1
        size = int(raw_input())
        arr.extend(raw_input().split(" "))

        print " ".join(frequency_sort(arr))


if __name__ == "__main__":
    main()