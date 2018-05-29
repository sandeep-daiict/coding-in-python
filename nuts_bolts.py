
e1?k1=1,k2=0,k3=2,k4=1
e2?k1=1,k2=0,k3=2,k4=1
e3?k1=1,k2=0,k3=2,k4=1

e1?k1=2,k2=0,k3=2,k4=1
e2?k1=3,k2=0,k3=2,k4=1
e3?k1=4,k2=0,k3=2,k4=1


k1  k2 k3 k4  e1 e2 e3
1    0  2  1  1  1  1
2   0  2   1 1  0  0
3   0  2   1 0  1  0
4   0   2  1 0  0  1
o 

Q1. Given 'n' nuts and 'n' bolts; what is the efficient mechanism to match nut with bolt. Given that there is only one exact match for a nut with bolt. When you try to match a nut and bolt you can get (1) if match is exact (2) nut is loose (3) nut is tight


n1,n2,n3,n4,n5,n6

b1,b2,b3,b4,b5,b6

bucket1 =  tights b1,b5           
bucket2 =  loose  b2,b3,b6 

n1<->b4


class Match {

Bolt bolt;
Nut nut;
}

public int matchBoltAndNut(Bolt bolt, Nut nut); // 0 if matches, 1 if nut is loose, -1 if nut is tight

List<Match> performMatch(List<Bolt> bolts, List<Nut> nuts) {

          performMatchRecur(bolts,nuts)

}

def performMatchRecur(bolts,nuts):
    if len(bolts)==0 and len(nuts) == 0:
        return
    n = nuts[0]
    low_bolt,high_bolt,result = getBucket(bolts, n, True)
    if len(low_bolt) == len(high_bolt) == 0:
        return result
    m = result[-1]
    b = m.bolt
    low_nut,high_nut,x = getBucket(nuts, b, False)
    if len(low_bolt) > 0:
        a = performMatchRecur(low_bolt,low_nut)
    if len(high_bolt) > 0:    
        b = performMatchRecur(high_bolt,high_nut)
    return a.extends(b)
    

def getBucket(parts, item, isnut):
    low_bucket = []
    high_bucket =[]
    result = []
    if len(parts)==1:
        m = Match()
        m.bolt = p
        m.nut = item
        result.append(m)
        return low_bucket,high_bucket,result
    for p in parts():
        if isnut:
            val = matchBoltAndNut(p,item)
            if val == 0:
                m = Match()
                m.bolt = p
                m.nut = item
                result.append(m)
            else if val>0:
                high_bucket.append(p)
            else:
                low_bucket.append(p)
        else:
            val = matchBoltAndNut(item,p)
            if val == 0:
                pass
            else if val>0:
                high_bucket.append(p)
            else:
                low_bucket.append(p)
                
    return low_bucket,high_bucket,result
                
        
        
        
        
        
        
        
        
        
        
        

