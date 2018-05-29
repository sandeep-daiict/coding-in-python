def find_phone_number(text):
    s = ""
    for i in text:
        if i.isdigit():
            s=s + '1'
        else:
            s=s + i
            
    index1 = s.find("111-111-1111")
    index2 = s.find("(111) 111-1111")
    
    if index1 < 0 and index2 < 0:
        return "NONE"
    if index1 >= 0 and index2 < 0:
        return text[index1:index1+12]
    if index1 < 0 and index2 >= 0:
        return text[index2:index2+14]
    if index1 < index2:
        return text[index1:index1+12]
    return text[index2:index2+14]
