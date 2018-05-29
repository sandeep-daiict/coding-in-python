def solution(array):
    size = len(array)
    if size <= 2:
        return ','.join([str(x) for x in array])
        
    output = []
    count = 1
    last_val = []
    last_val.append(str(array[0]))
    for i in range(1,size):
        if int(last_val[-1]) + 1 == array[i]:
            count = count + 1
            last_val.append(str(array[i]))
        else:
            if count>=3:
                output.append(str(last_val[0]) + "-"+ str(last_val[-1]))
                count = 1
                last_val = []
                last_val.append(str(array[i]))
            else:
                output.extend(last_val)
                count = 1
                last_val = []
                last_val.append(str(array[i]))
                
    if count>=3:
        output.append(str(last_val[0]) + "-"+ str(last_val[-1]))
        count = 1
        last_val = []
        last_val.append(str(array[i]))
    else:
        output.extend(last_val)
        count = 1
        last_val = []
        last_val.append(str(array[i]))
    
    return ','.join(output)

