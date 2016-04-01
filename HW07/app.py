def repeat(a):
	def x(b):
		return a*b
	return x

def r1(a):
	return repeat("hello")(a)

def r2(a):
        return repeat("goodbye")(a)
