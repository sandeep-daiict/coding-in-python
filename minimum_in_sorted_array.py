


def binary_search_rotation_util(arr, low , high):
    if low > high:
        return arr[0]

    mid = low + (high - low)/2
    if mid >= len(arr) or mid < 0:
        return arr[0]

    if arr[mid] < arr[mid - 1]:
        return arr[mid]

    a = binary_search_rotation_util(arr, low, mid - 1)
    b = binary_search_rotation_util(arr, mid + 1, high)

    if a != -1:
        return a
    if b != -1:
        return  b
    return arr[0]

def main():
    t = int(raw_input().strip())
    while t > 0:
        t = t - 1
        s = int(raw_input().strip())
        arr = [int(i) for i in raw_input().strip().split(" ")]
        print binary_search_rotation_util(arr,0,s)





if __name__ == "__main__":
    main()