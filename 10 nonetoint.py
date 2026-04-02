# we are going to convert none to int by using 

x=None
print(x)
print(type(x))

a=int(x)
print(type(a))
print(a)


# This program will give you a type error
'''TypeError: int()argument must be a string, bytes-like object or a real number, not NoneType means
:means you tried to convert a None value to an integer using the int() function in Python. 
None is a special constant in Python used to denote the absence of a value, and the int() function cannot convert this type.
'''