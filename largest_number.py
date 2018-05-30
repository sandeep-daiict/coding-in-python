
def main():
    test_cases = int(raw_input())
    while test_cases > 0:
        test_cases  = test_cases - 1
        size = int(raw_input())
        arr = []

        arr.extend(raw_input().split(" "))
        arr = sorted(arr, cmp = comp)
        print ''.join(arr)

def comp(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    if l1 == l2:
        if int(str1) > int(str2):
            return -1
        return 1
    else:
        a = str1+str2
        b = str2+str1
        return comp(a,b)

if __name__ == "__main__":
    main()