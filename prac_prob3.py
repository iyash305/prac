coordinates = (10,20)
print(coordinates[0])
print(coordinates[1]) 
corlist = list(coordinates)
print(corlist)
corlist[0] = 50 
print(corlist)
new_coordinates = tuple(corlist) 
print(new_coordinates)
