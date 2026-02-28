my_list = [1,2,2,2,4,4,5,1,6,8,9,7]
my_set = set(my_list)
print(my_set)

products = {
    "Laptop": 50000,
    "Phone": 20000,
    "Tablet": 30000
}

max_value = max(products.values())
print(max_value)

dict_1 = {
    "name": "yash",
     "age": 26     
     }
dict_2 = {
    "name": "tim",
    "game": "football"
}

d3 = {**dict_1,  **dict_2}
print(d3)


dict_1 = {"a": 1, "b": 2}
dict_2 = {"b": 100, "c": 3}

dict_1.update(dict_2)
print(dict_1)

list1 = [1, 2, 3]
list2 = list1

list2 = list2 + [4]

print(list1)
print(list2)