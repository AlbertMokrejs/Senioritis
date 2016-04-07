def union(a,b):
  return a + [x for x in b if x not in a];
  
def intersection(a,b):
  return [x for x in a if (x in a) and (x in b)];
  
def setDifference(a,b):
  return [x for x in a if x not in b];
  
def symDifference(a,b):
  return [x for x in a+b if (x in a)!=(x in b)];
  
def cartProduct(a,b):
  return [z for d in [[[x,y] for y in b] for x in a] for z in d];
  
