def reverse_str(s):
    if len(s) == 1:
        return s
    return s[-1] + reverse_str(s[0:-1])

print reverse_str(raw_input())
