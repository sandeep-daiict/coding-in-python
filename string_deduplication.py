def dedup(input_str, chunk_size):
    """
    Args:
        input_str (str): The string on which to deduplicate
        chunk_size(int): Dedup should be done in order of chunk size.
    
    Returns:
        The deduplicated string
    """
    # Write your code here
    m = {}
    s = len(input_str)
    location = 0
    for i in range(0,s,chunk_size):
        key = input_str[i:i+chunk_size]
        if key in m:
            m[key].append(str(location))
        else:
            m[key] = [str(location)]
            
        location = location + 1
    output = ""
    for key, value in m.iteritems():
        output = output + ','.join(value) +"|" + key +  ":"
    return output
    
def redup(deduplicated_str, chunk_size):
    """
    Args:
        deduplicated_str(str): The string from the dedup function
    
    Returns:
        The reconstructed original string
    """
    # Write your code here.
    
    m = {}
    chunks = deduplicated_str.split(":")
    max_loc = -1
    for c in chunks:
        if c is None or len(c) == 0:
            continue
        
        loc = c.split("|")[0].split(",")
        key = c.split("|")[1]
        for l in loc:
            lo = int(l)
            m[lo] = key
            if max_loc < lo:
                max_loc = lo
            
    
    output = ""
    for i in range(0,max_loc + 1):
        output = output + m[i]
    return output
