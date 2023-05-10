##########zero based indexing####################
t1=(10,20,30,40,50,60,70,80,90)
print(len(t1))
print(t1[0])
print(t1[1])
for i in range(len(t1)):
    print(t1[i])
print("#############by slicing##############")
############by slicing#########################
print(t1[2:7:1])
print(t1[2:7])
print(t1[2:7:2])
print(t1[2:])
print(t1[:7])
print(t1[::])
print(t1[::-1])
print("###########negative indexing###########")
print(t1[-1])
print(t1[-5])