#####reverse#########
mylist=[10,20,30,40,10,20,10,10]
print(mylist)
mylist.reverse()
print(mylist)
############sort#######
mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)
mylist1=['aaaaa','bb','cccc']
mylist1.sort(key=len)
print(mylist1)
def mysort(list1):
    return list1[1]
mylist2=[[2,9],[4,3],[8,2]]
print(mylist2)
mylist2.sort(key=mysort)
print(mylist2)
###########copy#############
list1=[1,2,3]
list2=list1
list2[0]=90
print(list1)
print(list2)
#######################
list1=[1,2,3]
list2=list1.copy()
list2[0]=90
print(list1)
print(list2)