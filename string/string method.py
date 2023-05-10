############ capitalize#########
s1="this IS DEMO STRING "
print(s1)
s2=s1.capitalize()
print(s2)
#########lower##########
s1="hello world"
print(s1)
print(s1.lower())
######upper###########
print(s1.upper())
#######swapcase#######
print(s1.swapcase())
#########title#######
print(s1.title())
#########count########
s1="hello world.hell this is demo"
x=s1.count("l")
print(x)
x=s1.count('hello')
print(x)

print('##########startwith###########')

print(s1.startswith('he'))
print(s1.startswith('hel'))
print(s1.startswith('ello'))

print('#########endwith############')
print(s1.endswith('demo'))
print(s1.endswith('emo'))
print(s1.endswith('dem'))

print("#########find############")
s1='This is string .This is demo'
x=s1.find('is')
print(x)
x=s1.rfind('is')
print(x)

print("############index###############")
x=s1.index('is')
print(x)
x=s1.rindex('is')
print(x)

print("############find all index#############")
s1="This is string.This is demo"
x=-1
while True:
    x=s1.find('is',x+1)
    print(x)
    if x==-1:
        break;

print("###########isalnum############")
s1="hello 123"
print(s1.isalnum())
print(s1.isalpha())
print(s1.isdigit())
s1='123'
print(s1.isdigit())
s1="hello"
print(s1.isupper())
print(s1.islower())
s1='\n \t'
print(s1.isspace())

print("########center,rjust,ljust###########")

s1="hello world"
print(s1.center(50,'*'))
print(s1.rjust(50,'*'))
print(s1.ljust(50,'*'))

print("#############lstrip,rstrip,strip#############")
s1=" hello vaishnavi  "
print(len(s1))
#####lstrip##########
s1=s1.lstrip()
print(len(s1))
#######rstrip############
s1=s1.rstrip()
print(len(s1))
s1="hello"
s1=s1.strip()
#########strip##########
s1="abc"
s2=" abc "
if s1==s2.strip():
    print("equals")
else:
    print("not equals")

print("###########join,split,split line,replace########")

###join####
mylist=['This','is','demo']
s1="".join(mylist)
print(s1)
s1=" ".join(mylist)
print(s1)
s1=", ".join(mylist)
print(s1)
#######split######
s1="a,b,c,w,d,y,f,l,v"
arr=s1.split(',')
print(arr)
#######splitline########
s1="This is demo,/n This is string"
arr=s1.splitlines()
print(arr)
########replace#############
s1="This is demo"
arr=s1.replace('is',"IS")
print(arr)