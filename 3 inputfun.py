# The input function is use to take data from the user 
#the input function is a build in function 

'''rollno=input("Enter your Roll Number")
print( rollno)


print("Enter your Roll Number")
rollno=input()
print("Your Roll Number is-->", rollno)'''

#to take multple value or inputs from the users we can use a single input for different values

# int1,int2,int3,int4 = input("Enter 4 values").split()


# print(int1)
# print(int2)
# print(int3)
# print(int4)

#in above program we have to use split function at the end because without split function the interpreter will show error


# in this program we will take input from the user and add them

'''n1= int(input("Enter a first number"))
n2= int(input("Enter second number"))

sum= (n1+n2)
print("The sum of the number is-->", sum)'''

#since the int funtion is used both the values are integers hence the addition will work correctlyotherwise it will not add the numbers

#we can also split the input function according to us like in the below program
a,b=input("enter name and college").split("*")
print(a)
print(b)




