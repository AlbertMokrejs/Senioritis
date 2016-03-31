import string

def isValid(p):
    return len([1 for x in [[ 1 for x in p if x in string.ascii_uppercase ],[ 1 for x in p if x in string.ascii_lowercase ],[ 1 for x in p if x in string.digits ]] if len(x) > 0])>2

def scoreValid(p):
    a = [1 for x in [[1 for x in [[ 1 for x in p if x in string.ascii_uppercase ]] if len(x) > 0] + [1 for x in [[1 for x in p if x in string.ascii_lowercase ]] if len(x) > 0]] if len(x) > 1]
    a += [1 for x in [[1 for x in p if x in ".?!&#,;:-_*"]] if len(x)>0]
    a += [1 for x in [[ 1 for x in p if x in string.digits ]] if len(x)>0]
    return len(a)*3 + 1

print isValid("aB3d")
print isValid("aaaaaa")
print scoreValid("aaaaa")
print scoreValid("aBCD4")
print scoreValid(";aBe4")
