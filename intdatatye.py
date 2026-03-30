# int data type , the int data type is used to represent integer value in the progaram 

'''If we want to know the type of the variable in the program we can use 'type' '''

a=20
print(a)
print(type(a))

# here the int is a class and the "a" is the object of the class int

"""The initial storage size of an int data type is 28

The size of type, refrence, padding is 8 byte and the size of value will increase
--> for the size you have to import sys """

import sys
b =10 
print(b)
print(type(b))
print(sys.getsizeof(b))
print(id(b))

a=10
print(a)
print(type(a))
print(id(a))
print(sys.getsizeof(a))

# we can use id functon to know the memory address of the object created in the class