numbers = [i for i in range(1,11)] 
print(numbers) 
print(numbers[0:2])
print(numbers[-3:])


coordinates = (10,20)
print(coordinates[0])
print(coordinates[1]) 
corlist = list(coordinates)
print(corlist)
corlist[0] = 50 
print(corlist)
new_coordinates = tuple(corlist) 
print(new_coordinates)

