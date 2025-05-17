#list = used to store multiple items in a single variable
from pkg_resources import non_empty_lines

# food = ["pizza" , "hamburger" , "hotdog"]
# print(food)
# food[0] = "sushi"
# print(food)

#print by loop
# for f in food:
#     print(f)
#
# food.append("icecream")
# food.remove("hotdog")
# food.pop() #last value is poped
# food.insert(1,"icecream")
# food.sort()
# food.clear()
# print(food)

#2D lists = a list of lists

# drinks = ["coffee", "milk","tea"]
# dinner = ["pizza" , "hamburger" , "hotdog"]
# dessert = ["cake" , "ice cream"]
#
# food = [drinks, dinner, dessert]
# print(food[0][2])

#tuple = collection which is ordered and unchangeable used to group together related data

student = ("isha" , 20 , "female")
print(type(student))
# print(student.count("female"))
# print(student.index("female"))
# student.remove("female")
# student.append("female")
# print(student)
#
# if "female" in student:
#     student.remove("female")

#set = collection which is unordered , unindexed . no duplicate values

# book = {"c" , "c++" ,"python"}
# dish = {"bowl" , "plate"}
# book.add("java")
# book.remove("java")
# book.clear()
# book.update(dish)
# dish.update(book)
# print(type(book))
# print(book)
# print(dish)

# dinner = book.union(dish)
# print(dinner)

# print(dish.difference(book))

#Dictionary = a changeable , unordered collection of unique key : value
#           pairs fast beacause they use hashin , allow us to access a value quickly


