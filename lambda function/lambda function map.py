list1=[1,2,3,4,5,6,7,8,9,10]
list2=list(map(lambda x:x*x,list1))
print(list2)
###################################
list1=[1,2,7,14,28,21,35]
list2=list(filter(lambda x:x%7==0,list1))
print(list2)
