########accessing dictionary element#######
d1={1:'abc',2:'xyz','c':200,(10,20):'hello'}
print(d1)
print(type(d1))

###########access dict items###########
print(d1[1])
print(d1['c'])
print(d1[(10,20)])
print(d1.get(1))

###########copy,update###########
d1={1:'abc'}
d2=d1.copy()
d2[1]='xyz'
print(d2)
print(d1)
###########update##########
d1={1:'abc'}
d2={1:'xyz',2:'pqr'}
print(d1)

#########set##############
#####access set element#####
s1={10,20,30,40,50,10,20,30,60}
print(s1)
print(type(s1))

######accessing items of set############
for x in s1:
    print(x)


