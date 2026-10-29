a=[1,2,3]
b=a
b[0]=99
print(a)
c=a.copy()
c[0]=10
print(a,b,c)