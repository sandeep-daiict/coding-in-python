import time
def next_number(string):
    if len(string) == 1:
        return "1" + string

    count = 0
    prev = string[0]
    output = ""
    for s in string:
        if s == prev:
            count=count+1
        else:
            output =output + str(count) + prev
            count = 1
            prev = s
    else:
        output = output + str(count) + prev
        count = 1
        prev = s
    return output



s = lambda string,a: next_number(string) 

def print_seq(n):
	initial = "1"
	for i in range(1,n):
		initial = next_number(initial)
	return initial



def with_lambda_print_seq(n):
	x = reduce(s, [str(i) for i in range(1,n+1)])

for i in range(1,101):
	t = time.time()
	a = with_lambda_print_seq(i)
	t2 = time.time()
	b = print_seq(i)
	print "lambda time= " + str(t2 - t)
	print "normal time= " + str(time.time() - t2)
