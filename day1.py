#some inportant useful functions
name = "Gaurav Kumar Tiwari"
print(len(name))
print(name.find("K"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("a"))
print(name.replace("a", "o"))
print(name*50)

#typecasting in python. Converting a data type of a value to another data type.
x = 1
y = 2.0
z = "3"

print(x)
print(y)
print(z*3)
print ("x and y is decimal " + str(x), str(y) + " and z is string " + z)

#taking user input in python 
age = input("How old are you?")
age = float(age)
age += 1
print("You are " + str(age) + " years old.")
name = input("What is your name?")
print ("My name is " + name+"." + " I am " + str(age) + " years old.")

# useful functions related to numbers using math module.

import math
pi = 3.14
x=1
y=2
z=3
print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi,2))
print(math.sqrt(pi))
print(max(x,y,z,pi))
print(min(x,y,z,pi))
print(type(z))


