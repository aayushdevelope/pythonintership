# Type casting is the process of converting one data type to another data type
 
'''type casting are of two type 
1.Implicit type casting : when python does casting or conversion automatically
2. Explici type casting : you have to convert one data type to another data type'''

'''for convertion one data type to another we have to use some build in function 
like int(), float(), str(),bool()'''
#Converting float to int (by expicit conversion)

a=10.5
print(a)
print(type(a))

b=int(a)
print(b)
print(type(b))

b=100.5
print(b)
print(type(b))
c=int(b)
print(c)
print(type(c))



#converting float to int by Implicit conversion

a=10
b=10.5
print(type(a))
print(type(b))
sum=a+b
print(sum)
print(type(sum))


mul=a*b
print(mul)
print(type(mul))