# # main.py file
# from mymodule import generate_full_name, sum_two_nums, person, gravity
# print(generate_full_name('Asabneh','Yetayeh'))
# print(sum_two_nums(1,9))
# mass = 100;
# weight = mass * gravity
# print(weight)
# print(person['firstname'])

# main.py file
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100;
weight = mass * g
print(weight)
print(p)
print(p['firstname'])