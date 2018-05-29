s = raw_input()
def perm(a,l,r):
	if l==r:
		print ''.join(a)
	for i in range(l,r):
		a[l],a[i]=a[i],a[l]
		perm(a,l+1,r)
		
		a[l],a[i]=a[i],a[l]

perm(list(s),0,len(s))
