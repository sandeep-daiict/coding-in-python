#https://practice.geeksforgeeks.org/problems/how-many-xs/0


t = int(raw_input().strip())
while t > 0:
    t = t - 1
    x = raw_input().strip()
    val = raw_input().strip().split(" ")
    s = ""
    for i in range(int(val[0]) + 1, int(val[1])):
        s = s + str(i)
    print(s.count(x))
