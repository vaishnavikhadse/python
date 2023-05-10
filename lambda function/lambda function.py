#without lambda fuction

def check(list2):
    temp=[]
    for x in list2:
     if x%2==0:
        temp.append(x)
     return temp
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list3=check(list1)
    print(list3)
#######with lammda function##########
list1=[1,2,3,4,5,6,7,8,9,10]
list2=list(filter(lambda x:x%2==0,list1))
print(list2)