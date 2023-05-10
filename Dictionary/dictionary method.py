d1={1:'abc',2:'xyz',3:'pqr'}
print(d1)
#######key#############
print("*key*")
mkeys=d1.keys()
for k  in mkeys:
    print(k)

print("*values*")
mvalue =d1.values()
for v in mvalue:
    print (v)

print("*key+values")
mitems=d1.items()
for k,v in mitems:
    print(k,v)

print("*pop,popitem,clear")

d1={1:'abc',2:'xyz',3:'pqr',4:'qqq',5:'rrr'}
print(d1)
d1.pop(2)
print(d1)
d1.popitem()
print(d1)
###########by using del keyword#########
del d1[1],d1[4]
print(d1)
#####clear############
d1.clear()
print(d1)