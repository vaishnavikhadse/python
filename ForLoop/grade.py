m1=int(input("enter mark1"))
m2=int(input("enter mark2"))
m3=int(input("enter mark3"))
m4=int(input("enter mark4"))
m5=int(input("enter mark5"))
p=(m1+m2+m3+m4+m5)/5
if   p>=90:
    print("grade A")
elif p>=80:
    print("grade B")
elif p >= 70:
    print("grade C")
elif p>=60:
    print("grade D")
elif p>=40:
    print("grade E")
else:
    print("grade F")

