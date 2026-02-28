my_set = {1,2,3,3,4}
my_set.add(5)
print(my_set)
my_set.remove(2)
if 4 in my_set:
    print("Present")


a = {1,2,3}
b = {3,4,5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))