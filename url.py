num = int(raw_input())
urls = []
for i in range(num):
    urls.append(raw_input())
d = {}
for url in urls:
    if url in d:
        d[url] = d[url] + 1
    else:
        d[url] = 1
print len(d)
for k,v in sorted(d.items(), key = lambda(x): (-x[1], x[0])):
    print k
