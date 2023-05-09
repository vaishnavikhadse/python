print("##################################################################")
for i in range(1,5):
   for j in range(1,5):
     if i==1 or i==4 or j==1 or j==4:
        print('*',end=' ')
     else:
        print(' ',end=' ')
   print( )
print("##################################################################")
for i in range(1,6):
   for j  in range (1,6):
     if i==j or i+j==6:
        print('*',end=' ')
     else:
        print(' ',end=' ')
   print( )
print("######################################################################")
for i in range (1,6):
    for j in range (1,4):
      if j==1 or i==1 or i==3 or i==5:
          print('*',end=' ')

      else:
        print(' ',end=' ')
    print()
print("#############################################################################")
