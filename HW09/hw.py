import time

def timer(f):
    def inner(*arg):
        t = time.time()
        out = f(*arg)
        print "Time: " + str(t-time.time()) + " seconds"
        return out
    return inner

def namer(f):
    def inner(*arg):
        print "Name: " + f.func_name + ", Params: (" + str([x for x in arg])[1:][::-1][1:][::-1] +")"
        return f(*arg)
    return inner

def a(*arg):
    return [x*x for x in arg]

timer(a)(2,3,4)
namer(a)(2,3,4)
