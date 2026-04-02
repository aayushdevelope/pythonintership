# In this program we will convert string to int type

st="1000"
print(st)
print(type(st))

bal=int(st)
print(bal)
print(type(bal))

# in string we can only convert numric value to int we cannot convert non numric,alphanumric, 
# characters, and letter to int from string

'''problematic case in string when we convert it into int'''

st=""
print(st)
print(type(st))

x=int(st)
print(x)
print(type(x))

# An empty string cannot be converted into int it will give an value error
'''it will give a value error: invalid litera for int() with base 10 which means 
means you tried to convert a string into an integer, but the string's content was
 not a valid whole number in the decimal (base 10) system'''

st="Hello123"
print(type(st))

a=int(st)
print(x)
print(type(x))

# it wil also give type error becouse we cannot use alpha numric value to convert it into int

a="True"
b=int(a)
print(b)



