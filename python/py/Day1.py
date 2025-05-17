# print("Hello World")
# print("ISHA PRAJAPATI")
# print("B.TECH STUDENT")

#variable = a container for a value.
# Behaves as the value that it contains

#String datatype
# first_name = "ISHA"
# last_name = "PRAJAPATI"
# full_name = first_name + " " + last_name
# print("Hello "+ full_name)
# print(type(full_name))

#Int datatype
#age = 19
# age = age + 1
# print("My Age in 2025 is :",age)
#print("My Age in 2025 is :"+str(age))
# print(type(age))

#Float datatype
# weight = 39.200
# print("My weight is :",weight,"kg")
# print(type(weight))

#Boolean
# isgood = True
# print("I am good girl? : ",isgood)
# print(type(isgood))

#multiple assignmnt = allows us to assign multiple variable at the same time in one line of code
# name = "ISHA"
# age = 19
# dob = "15th march 2005"

# name,age,dob = "isha" , 19 , "15th march"
# print(name)
# print(age)
# print(dob)
#
# maths = chemistry = physics = 100
# print(maths)
# print(chemistry)
# print(physics)

#in built function
# name = "ISHA PRAJAPATI"
# print(name)
# print(len(name))
# print(name.find("P"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("P"))
# print(name.replace("I" , "A"))
# print(name*2)

#type casting = convert the data type of a value to another data type
# x = 1
# y = 100.0
# z = "1000000"

# print(x,y,z)
# print(type(x),type(y),type(z))

# x= str(x)
# y = str(y)
# # z = int(z)
# print(x,y,z)
# print(type(x),type(y),type(z))
# print(z*3)

#input
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# height= float(input("Enter your height: "))
# print("Hello " + name)
# print(name +" age is " + str(age))
# print(name , " height is " ,  height , "cm")

# import math
# pi = 3.14
# x=1
# y=2
# z=3
# print(pi)
# print(type(pi))
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(math.trunc(pi))
# print(abs(pi))
# print(abs(-pi))
# print(pow(pi,2))
# print(math.sqrt(pi))
# print(max(x,y,z))
# print(min(x,y,z))

#slicing = create a substring by extracting elements from another string
            # indexing[] or slice()
            # [start:stop:step]

#indexing
# name = "isha prajapati"
# print(name)
# first_name= name[0:4]
# print(first_name)
# first_name= name[-1:-6]
# print(first_name)
# first_name= name[-6:-4]
# print(first_name)
# first_name= name[:4]
# print(first_name)
# first_name= name[4:]
# print(first_name)
# first_name= name[0:4:2]
# print(first_name)
# first_name= name[::3]
# print(first_name)
# first_name= name[::-1]
# print(first_name)

#slicing
# website = "hello.com"
# slice = slice(0,10,2)
# print(website[slice])

#if statement = a block of code that will execute if it's condition is true

# age = int(input("Enter your age : "))
# if age >= 18:
#     print("you are adult!!")
# elif age< 0:
#     print("you are not born yet!!")
# else:
#     print("you are child!!")