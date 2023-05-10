s1='This is string'
s2="This is also string"
s3="""This is multiline string1
This is multiline string 2"""
print(type(s1))
print(type(s2))
print(type(s3))

print("####### string interpolation#########")
fname="abc"
age=60
s1="hello{fname} your age is{age}"
print(s1)