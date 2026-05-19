# a)
list_a = list(range(2, 20))

# б)
list_b = [x**2 for x in range(1, 11)]

# в)
list_c = [x**2 for x in range(10, -1, -1)]

# г)
list_d = [x for x in range(101) if x % 2 != 0 and x % 3 != 0 and x % 5 != 0]

print("a)", list_a)
print("б)", list_b)
print("в)", list_c)
print("г)", list_d)