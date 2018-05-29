def isNeat(num):
    prev =''
    for i in range(len(num)):
        if i==0:
            prev = num[i]
        else:
            if int(prev) > int(num[i]):
                return False
            else:
                prev = num[i]
    return True


number = int(raw_input())

number_str = str(number)
prev = ""
for i in range(len(number_str)):
    if i == 0:
        prev = prev + number_str[0]
    else:
        if int(prev[-1]) <= int(number_str[i]):
            prev = prev + number_str[i]
        else:
            break;

prev = str(int(prev) - 1)
while True:
    if len(prev) == 0 or isNeat(prev) == True:
        break
    prev = prev[:-1]
    prev = str(int(prev) - 1)

print int(prev + "9"*(len(number_str) - len(prev)))
