##########add############

s1={10,20,30,40,50,60}
print(type(s1))
s2=set([1,2,3])
print(type(s2))

######add#############
s1.add(90)
s1.add('abc')
print(s1)

#########update###########
s1.update([7,8,9])
s1.update([77,87,97])
s1.update(["hello"])
print(s1)
##########remove ,discard#############
s1={10,20,30}
print(s1)
#s1.remove(30)
s1.discard(30)
print(s1)
##########pop and clear##############
s1={10,20,30,40}
print(s1)
s1.pop()
print(s1)
s1.clear()
print(s1)