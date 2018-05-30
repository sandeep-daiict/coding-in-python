class contact_book:
    count = 0
    contact_map = {}
    def printf(self):
        print self.count
        if self.contact_map is not None:
            for k in self.contact_map:
                print k
                self.contact_map[k].printf()
            
    
n = int(raw_input().strip())
cb = contact_book()
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if op == "add":
        current_map = cb.contact_map
        cb.count = cb.count + 1
        for c in contact:
            if c in current_map:
                current_map[c].count = current_map[c].count + 1
                current_map = current_map[c].contact_map
            else:
                cn = contact_book()
                cn.count = 1
                cn.contact_map = {}
                current_map[c] = cn
                current_map = cn.contact_map
    
    elif op == "find":
        current_map = cb.contact_map
        count = 0
        flag = True
        for c in contact:
            if c in current_map:
                count = current_map[c].count
                current_map = current_map[c].contact_map
                
            else:
                flag = False
        if flag:
            print count
        else:
            print 0
                
                
