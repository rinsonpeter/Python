from functools import *
y=filter(lambda x:x<4,[1,2,3,3,4,4,5])
print(tuple(y))
print(list(y))


r=reduce(lambda x,y:x+y,map(lambda x:x+x,filter(lambda x:x<=5,[1,2,3,4,5,6,7])))
print(r)