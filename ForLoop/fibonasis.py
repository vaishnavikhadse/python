n=int(input("enter a number"))
i=1
first=0
second=1
print(first,second,end=' ')
while i<=n:
    next=first+second
    print(next,end=' ')
    first=second
    second=next
    i=i+1