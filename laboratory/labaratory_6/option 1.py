my_list = [1, 5, 87, 32]
my_list[1] = 13
my_list.append(25)
my_list[1:2] = [4, 5]
del my_list[3:5]
my_list.insert(2, 8)
my_tuple = tuple(my_list)
print(my_tuple)
my_list.extend(my_tuple)
my_list.pop()
print(my_list)
print(my_tuple[::-1])